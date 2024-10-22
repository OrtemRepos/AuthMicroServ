import asyncio

from concurrent.futures import ThreadPoolExecutor, Executor


from typing import Callable, Awaitable
from abc import abstractmethod, ABC

from src.core.domain.entities import DomainEntityType


class ExecutorInterface(ABC):
    @abstractmethod
    async def execute(
        self,
        method: Callable[..., DomainEntityType],
        *args: tuple[any, ...],
        **kwargs: dict[str, any],
    ) -> DomainEntityType | Awaitable[DomainEntityType]:
        pass


class AsyncExecutor(ExecutorInterface):
    def __init__(
        self,
        loop: asyncio.AbstractEventLoop = None,
        executor: Executor = ThreadPoolExecutor(),
    ):
        self._loop = loop or asyncio.get_event_loop()
        self._executor = executor

    async def execute(
        self,
        method: Callable[..., DomainEntityType],
        *args: tuple[any, ...],
        **kwargs: dict[str, any],
    ) -> DomainEntityType | Awaitable[DomainEntityType]:
        if asyncio.iscoroutinefunction(method):
            return await method(*args, **kwargs)
        else:
            return await self._loop.run_in_executor(
                executor=self._executor, func=method, *args, **kwargs
            )
