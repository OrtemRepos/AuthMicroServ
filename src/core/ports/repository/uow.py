from abc import abstractmethod
from typing import Any, Protocol

from src.core.ports.repository import CommandRepositoryType


class UnitOfWorkInterface(Protocol):
    @abstractmethod
    def __init__(self, client: Any, repository: CommandRepositoryType) -> None:
        pass

    @abstractmethod
    def __enter__(self):
        pass

    @abstractmethod
    def __exit__(self, exc_type, exc_value, traceback):
        pass

    @abstractmethod
    async def __aenter__(self):
        pass

    @abstractmethod
    async def __aexit__(self, exc_type, exc_value, traceback):
        pass

    @abstractmethod
    async def commit(self):
        pass

    @abstractmethod
    async def rollback(self):
        pass
