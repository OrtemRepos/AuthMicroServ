import asyncio
from typing import Any
from uuid import UUID, uuid4

from loguru import logger

from src.core.cqrs.query import QueryType
from src.core.ports.event_bus import EventBusQueue
from src.infrastructure.query import HandlerFuncType, QueryRouter
from src.infrastructure.worker import Worker


class QueryBus(EventBusQueue[QueryType, HandlerFuncType, QueryRouter]):
    def __init__(
        self,
        event_router: QueryRouter,
        queue: asyncio.Queue,
        worker_num: int,
        retry_num: int,
        retry_timeout: int,
        result_queue: asyncio.Queue,
    ) -> None:
        super().__init__(
            event_router,
            queue,
            worker_num,
            retry_num,
            retry_timeout,
            result_queue=result_queue,
        )
        self._result_dict: dict[UUID, Any] = {}

    def _create_worker(
        self,
        name: str,
        router: QueryRouter | None = None,
        retry_num: int | None = None,
        retry_timeout: int | None = None,
    ) -> Worker[QueryRouter]:
        router = router or self._event_router
        retry_num = retry_num or self._retry_num
        retry_timeout = retry_timeout or self._retry_timeout
        worker = Worker[QueryRouter](
            name=name,
            router=router,
            queue=self._queue,
            retry_num=retry_num,
            retry_timeout=retry_timeout,
            result_queue=self._result_queue,
        )
        return worker

    def subscribe(
        self, event_type: type[QueryType], handlers: list[HandlerFuncType]
    ) -> bool:
        return self._event_router.register(event_type, handlers)

    async def _mapping_result(self) -> None:
        while self.is_running:
            event_id, result = await self._result_queue.get()
            self._result_dict[event_id] = result

    async def _get_result(self, event_id: UUID) -> Any:
        retry_counter = 0
        result = None
        while retry_counter < self._retry and not result:
            try:
                await asyncio.wait_for(
                    lambda: event_id in self._result_dict,
                    timeout=self.retry_timeout,
                )
                result = self._result_dict[event_id]
            except TimeoutError as e:
                retry_counter += 1
                logger.exception(
                    f"[{self.__class__.__name__}]\tException in QueryBus"
                    f"\nTry:\t{retry_counter}/{self._retry}",
                    e,
                )
        if retry_counter == self._retry and not result:
            logger.error(
                f"[{self.__class__.__name__}]\tMax retries exceeded for "
                f"key {event_id}."
            )

    async def publish(self, event: QueryType) -> Any:
        event_id = uuid4()
        await self._queue.put((event_id, event))
        return await self._get_result(event_id)
