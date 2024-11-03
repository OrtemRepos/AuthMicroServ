from abc import abstractmethod
from typing import Protocol

from src.core.cqrs.command import CommandType
from src.infrastructure.command import CommandRouter, HandlerFuncType


class WorkerInterface:
    async def start(self):
        pass

    async def stop(self):
        pass

    async def _worker_loop(self):
        pass


class CommandBus(Protocol):
    router: CommandRouter

    @abstractmethod
    def __init__(self, command_router: CommandRouter) -> None:
        pass

    @abstractmethod
    async def publish(self, event: CommandType) -> None:
        pass

    @abstractmethod
    def subscribe(
        self, event_type: type[CommandType], handlers: list[HandlerFuncType]
    ) -> bool:
        pass
