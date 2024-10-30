from src.infrastructure.query import QueryRouter
from src.core.cqrs.query import QueryType
from typing import Protocol, Any
from abc import abstractmethod


class QueryBus(Protocol[QueryType]):
    router: QueryRouter

    @abstractmethod
    def __init__(self, query_router: QueryRouter) -> None:
        pass

    @abstractmethod
    async def ask(self, command: QueryType) -> Any:
        pass
