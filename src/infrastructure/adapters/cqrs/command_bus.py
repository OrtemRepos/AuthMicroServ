import asyncio

from src.core.cqrs.command import CommandType
from src.core.ports.event_bus import EventBusQueue
from src.infrastructure.command import CommandRouter, HandlerFuncType


class CommandBus(EventBusQueue[CommandRouter, HandlerFuncType, CommandType]):
    def __init__(self, event_router: CommandRouter, queue: asyncio.Queue, worker_num: int, retry_num: int, retry_timeout: int) -> None:
        super().__init__(event_router, queue, worker_num, retry_num, retry_timeout)

    
    def subscribe(self, event_type: type[CommandType], handlers: list[HandlerFuncType]) -> bool:
        return self._event_router.register(event_type, handlers)