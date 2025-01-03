import asyncio
from abc import ABC, abstractmethod
from collections.abc import Awaitable, Callable
from concurrent.futures import Executor
from functools import singledispatchmethod
from typing import Generic, TypeVar

from src.core.domain.entities.aggregates import DomainEntityType

TDomain = TypeVar("TDomain", bound=DomainEntityType)

type SyncMethod[TDomain] = Callable[..., TDomain]
type AioMethod[TDomain] = Callable[..., Awaitable[TDomain]]


class ExecutorInterface(ABC, Generic[TDomain]):
    @singledispatchmethod
    @abstractmethod
    async def execute(
        self, method: SyncMethod[TDomain] | AioMethod[TDomain], *args
    ):
        pass


class AsyncExecutor(ExecutorInterface[TDomain]):
    def __init__(
        self,
        executor: Executor,
        loop: asyncio.AbstractEventLoop | None = None,
    ):
        self._loop = loop or asyncio.get_event_loop()
        self._executor = executor

    @singledispatchmethod
    async def execute(
        self, method: SyncMethod[TDomain] | AioMethod[TDomain], *args
    ):
        raise TypeError(
            f'Argument "method" have incompatible type "{type(method)}"'
            f'Expected "{SyncMethod[TDomain] | AioMethod[TDomain]}"'
        )

    @execute.register
    async def _sync(
        self, method: SyncMethod[TDomain], *args
    ) -> TDomain | None:
        return await self._loop.run_in_executor(self._executor, method, *args)

    @execute.register
    async def _aio(self, method: AioMethod[TDomain], *args) -> TDomain | None:
        return await method(*args)
