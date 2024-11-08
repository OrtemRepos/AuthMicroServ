import asyncio

from src.core.cqrs.command import CommandType
from src.core.ports.event_bus import EventBusQueue
from src.infrastructure.command import CommandRouter, HandlerFuncType
from src.infrastructure.worker import Worker


class CommandBus(EventBusQueue[CommandType, HandlerFuncType, CommandRouter]):
    def __init__(
        self,
        event_router: CommandRouter,
        queue: asyncio.Queue,
        worker_num: int,
        retry_num: int,
        retry_timeout: int,
    ) -> None:
        super().__init__(
            event_router, queue, worker_num, retry_num, retry_timeout
        )

    def subscribe(
        self, event_type: type[CommandType], handlers: list[HandlerFuncType]
    ) -> bool:
        return self._event_router.register(event_type, handlers)

    async def publish(self, event: CommandType) -> None:
        self._queue.put(event)

    def _create_worker(
        self,
        name: str,
        router: CommandRouter | None = None,
        retry_num: int | None = None,
        retry_timeout: int | None = None,
    ) -> Worker[CommandRouter]:
        router = router or self._event_router
        retry_num = retry_num or self._retry_num
        retry_timeout = retry_timeout or self._retry_timeout
        worker = Worker[CommandRouter](
            name=name,
            router=router,
            queue=self._queue,
            retry_num=retry_num,
            retry_timeout=retry_timeout,
        )
        return worker
