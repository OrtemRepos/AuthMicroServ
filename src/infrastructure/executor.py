import asyncio

from concurrent.futures import ThreadPoolExecutor, Executor


from typing import Callable
from abc import abstractmethod, ABC

from src.core.domain.entities import DomainEntityType


class ExecutorInterface(ABC):
    @abstractmethod
    async def execute(
        self, method: Callable[..., DomainEntityType], *args
    ) -> DomainEntityType | None:
        pass


class AsyncExecutor(ExecutorInterface):
    def __init__(
        self,
        loop: asyncio.AbstractEventLoop | None = None,
        executor: Executor = ThreadPoolExecutor(),
    ):
        self._loop = loop or asyncio.get_event_loop()
        self._executor = executor

    async def execute(
        self, method: Callable[..., DomainEntityType], *args
    ) -> DomainEntityType | None:
        if asyncio.iscoroutinefunction(method):
            return await method(*args)
        else:
            return await self._loop.run_in_executor(self._executor, method, *args)
