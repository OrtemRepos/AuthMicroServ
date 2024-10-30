from src.infrastructure.command import CommandRouter
from src.core.cqrs.command import CommandType
from typing import Protocol
from abc import abstractmethod


class CommandBus(Protocol[CommandType]):
    router: CommandRouter

    @abstractmethod
    def __init__(self, command_router: CommandRouter) -> None:
        pass

    @abstractmethod
    async def dispatch(self, command: CommandType) -> None:
        pass
