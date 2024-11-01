from abc import abstractmethod
from typing import Any, Protocol

from src.core.cqrs.query import QueryType
from src.infrastructure.query import QueryRouter


class QueryBus(Protocol[QueryType]):
    router: QueryRouter

    @abstractmethod
    def __init__(self, query_router: QueryRouter) -> None:
        pass

    @abstractmethod
    async def ask(self, command: QueryType) -> Any:
        pass
