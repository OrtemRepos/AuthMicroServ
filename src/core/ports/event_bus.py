import asyncio
from abc import ABC, abstractmethod
from typing import Generic, Protocol, TypeVar

from loguru import logger

from src.core.cqrs.command import CommandType
from src.core.cqrs.query import QueryType
from src.infrastructure.command import CommandRouter
from src.infrastructure.command import (
    HandlerFuncType as HandlerFuncCommandType,
)
from src.infrastructure.query import HandlerFuncType as HandlerFuncQueryType
from src.infrastructure.query import QueryRouter

RouterType = TypeVar("RouterType", CommandRouter, QueryRouter)
HandlerFuncType = TypeVar(
    "HandlerFuncType", bound=HandlerFuncQueryType | HandlerFuncCommandType
)
EventType = TypeVar("EventType", CommandType, QueryType, contravariant=True)


class WorkerInterface(Protocol):
    async def start(self):
        pass

    async def stop(self):
        pass

    async def _worker_loop(self):
        pass


class EventBusInterface(Protocol[EventType, HandlerFuncType]):
    @abstractmethod
    async def publish(self, event: EventType) -> None:
        pass

    @abstractmethod
    def subscribe(
        self, event_type: type[EventType], handlers: list[HandlerFuncType]
    ) -> bool:
        pass


class EventBusQueue(
    EventBusInterface, ABC, Generic[EventType, HandlerFuncType, RouterType]
):
    def __init__(
        self,
        event_router: RouterType,
        queue: asyncio.Queue,
        worker_num: int,
        retry_num: int,
        retry_timeout: int,
    ) -> None:
        self._event_router: RouterType = event_router
        self._queue = queue
        self._worker_num = worker_num
        self._retry_num = retry_num
        self._retry_timeout = retry_timeout
        self._workers: list[WorkerInterface] = [
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
    def retry_num(self, value: int):
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
            logger.warning(
                '"retry_timeout" must be greater than or equal to 0.'
            )
            self._retry_timeout = 0
        self._retry_timeout = value

    async def publish(self, event: EventType) -> None:
        if self._is_running:
            await self._queue.put(event)
        else:
            logger.warning(
                f"[{self.__class__.__name__}]\tPooling stop right now",
                self._is_running,
            )

    @abstractmethod
    def _create_worker(
        self,
        name: str,
        router: RouterType | None = None,
        retry_num: int | None = None,
        retry_timeout: int | None = None,
    ) -> WorkerInterface:
        pass

    @abstractmethod
    def subscribe(
        self, event_type: type[EventType], handlers: list[HandlerFuncType]
    ) -> bool:
        pass

    async def start(self):
        for worker in self._workers:
            worker.start()

    async def _gracefull_stop(self):
        self._is_running = False

        logger.info("Waiting for tasks to complete to stop gracefully")

        await self._queue.join()

    async def shutdown(self, gracefull: bool = True):
        logger.info("Shutdown polling", gracefull)
        if gracefull:
            await self._gracefull_stop()

        for worker in self._workers:
            worker.stop()
