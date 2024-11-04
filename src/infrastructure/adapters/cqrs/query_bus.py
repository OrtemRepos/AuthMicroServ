import asyncio

from src.core.cqrs.query import QueryType
from src.core.ports.event_bus import EventBusQueue
from src.infrastructure.query import QueryRouter, HandlerFuncType
from src.infrastructure.worker import Worker


class QueryBus(EventBusQueue[QueryRouter, HandlerFuncType, QueryType]):
    def __init__(self, event_router: QueryRouter, queue: asyncio.Queue, worker_num: int, retry_num: int, retry_timeout: int) -> None:
        super().__init__(event_router, queue, worker_num, retry_num, retry_timeout)

    
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
        )
        return worker

    def subscribe(self, event_type: type[QueryType], handlers: list[HandlerFuncType]) -> bool:
        return self._event_router.register(event_type, handlers)