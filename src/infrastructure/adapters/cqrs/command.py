import asyncio

from loguru import logger

from src.core.cqrs.command import CommandType
from src.core.ports.command.command_bus import CommandBus, WorkerInterface
from src.infrastructure.command import CommandRouter, HandlerFuncType


class Worker(WorkerInterface):
    def __init__(
        self,
        name: str,
        router: CommandRouter,
        queue: asyncio.Queue,
        retry_num: int,
        retry_timeout: int,
    ) -> None:
        self._name = name
        self._router = router
        self._queue = queue
        self._task: asyncio.Task | None = None
        self._is_running: bool = False
        self._retry = retry_num
        self._retry_timeout = retry_timeout

    @property
    def retry(self) -> int:
        return self._retry

    @retry.setter
    def retry(self, value: int):
        if value < 0:
            logger.warning('"retry" must be greater than or equal to 0.')
            self._retry = 0
        self._retry = value

    @property
    def retry_timeout(self):
        return self._retry_timeout

    @retry_timeout.setter
    def retry_timeout(self, value: int):
        if value < 0:
            logger.warning('"retry_timeout" must be greater than or equal to 0.')
            self._retry_timeout = 0
        self._retry_timeout = value

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if self._is_running:
            logger.warning(
                f"You can not change the name of worker {self._name} while it is running."
            )
            return
        self._name = value

    @property
    def is_running(self) -> bool:
        return self._is_running

    @is_running.setter
    def is_running(self, value: bool):
        if self._is_running and not value:
            self.stop()
        elif not self._is_running and value:
            self.start()
        else:
            str_for_log = f"[{self.__class__.__name__}] Worker already"
            if self._is_running:
                str_for_log += "running"
            else:
                str_for_log += "stopped"
            logger.warning(str_for_log, self._is_running)

    def start(self):
        if self._task and self._is_running:
            return
        self._is_running = True
        self._task = asyncio.create_task(self._worker_loop())
        logger.info(f"[{self.__class__.__name__}]\tWorker {self._name} started")

    def stop(self):
        if self._task and self._is_running:
            self._task.cancel("Stopping worker")
            self._is_running = False
            self._task = None
            logger.warning(
                f"[{self.__class__.__name__}]\tStopping worker {self._name}."
            )

    async def _worker_loop(self):
        while self._is_running:
            retry_counter = 0
            event = await self._queue.get()
            while retry_counter < self._retry:
                try:
                    await self._router.execute(event)
                    break
                except Exception as e:
                    retry_counter += 1
                    logger.exception(
                        f"[{self.__class__.__name__}]\tException in worker {self._name}.\nTry:\t{retry_counter}",
                        e,
                    )
                    await asyncio.sleep(self._retry_timeout)
            if retry_counter == self._retry:
                logger.error(
                    f"[{self.__class__.__name__}]\tMax retries exceeded for command {event} in worker {self._name}"
                )
            self._queue.task_done()


class CommandBusQueue(CommandBus):
    def __init__(
        self,
        command_router: CommandRouter,
        queue: asyncio.Queue,
        worker_num: int,
        retry_num: int,
        retry_timeout: int,
    ) -> None:
        self._command_router = command_router
        self._queue = queue
        self._worker_num = worker_num
        self._retry_num = retry_num
        self._retry_timeout = retry_timeout
        self._workers: list[Worker] = [
            self._create_worker(f"worker-{i}") for i in range(worker_num)
        ]
        self._is_running = False

    @property
    def is_running(self) -> bool:
        return self._is_running

    @is_running.setter
    async def is_running(self, value: bool):
        if self._is_running and not value:
            await self.shutdown(gracefull=True)
        elif not self._is_running and value:
            self.start()
        else:
            str_for_log = f"[{self.__class__.__name__}]\t alredy"
            if self._is_running:
                str_for_log += " running"
            else:
                str_for_log += " stopped"
            logger.warning(str_for_log, self._is_running)
    
    @property
    def retry_num(self) -> int:
        return self._retry_num
    

    @retry_num.setter
    def retry(self, value: int):
        if value < 0:
            logger.warning('"retry" must be greater than or equal to 0.')
            self._retry = 0
        self._retry = value

    @property
    def retry_timeout(self):
        return self._retry_timeout

    @retry_timeout.setter
    def retry_timeout(self, value: int):
        if value < 0:
            logger.warning('"retry_timeout" must be greater than or equal to 0.')
            self._retry_timeout = 0
        self._retry_timeout = value
    

    async def publish(self, event: CommandType) -> None:
        if self._is_running:
            await self._queue.put(event)
        else:
            logger.warning(
                f"[{self.__class__.__name__}]\tStop CommandBus right now",
                self._is_running,
            )

    def _create_worker(
        self,
        name: str,
        router: CommandRouter | None = None,
        retry_num: int | None = None,
        retry_timeout: int | None = None,
    ):
        router = router or self._command_router
        retry_num = retry_num or self._retry_num
        retry_timeout = retry_timeout or self._retry_timeout
        worker = Worker(
            name=name,
            router=router,
            queue=self._queue,
            retry_num=retry_num,
            retry_timeout=retry_timeout,
        )
        return worker

    def subscribe(
        self, event_type: type[CommandType], handlers: list[HandlerFuncType]
    ) -> bool:
        return self._command_router.register(event_type, handlers)

    async def start(self):
        for worker in self._workers:
            worker.start()

    async def _gracefull_stop(self):
        self._is_running = False

        logger.info("Waiting for tasks to complete to stop gracefully")

        await self._queue.join()

    async def shutdown(self, gracefull: bool = True):
        logger.info("Shutdown CommandBus", gracefull)
        if gracefull:
            await self._gracefull_stop()

        for worker in self._workers:
            worker.stop()
