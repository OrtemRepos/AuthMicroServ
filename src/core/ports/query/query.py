from typing import Protocol, Callable
from abc import abstractmethod
from functools import wraps, lru_cache
from core.domain.entities import DomainEntityType
from src.core.cqrs.query import QueryType
from src.core.ports import Dependencies


class QueryHandler(Protocol[QueryType, DomainEntityType]):
    @abstractmethod
    async def execute(Query: QueryType) -> DomainEntityType:
        pass


class QueryHandlerFactory:
    def __init__(self) -> None:
        self._handlers_factory: dict[
            tuple[QueryType, Dependencies], Callable[[Dependencies], QueryHandler]
        ] = {}

    def query_handler(self):
        def decorator(
            func: Callable[[QueryType, Dependencies | None, QueryHandler], None],
        ):
            @wraps
            def wrapper(
                type_query: QueryType,
                domain_entity: DomainEntityType,
                dependencies: Dependencies,
                base_class: QueryHandler = QueryHandler,
            ):
                class QueryHandlerImpl(base_class[type_query, domain_entity]):
                    def __init__(
                        self, dependencies: Dependencies | None = dependencies
                    ):
                        self.dependencies = dependencies or {}
                        self.func = func

                    async def execute(self, query: type_query):
                        return await self.func(query, self.dependencies)

                self.register(
                    type_query, lambda dependencies: QueryHandlerImpl(dependencies)
                )

            return wrapper

        return decorator

    def register(
        self,
        type_query: type,
        handler_factory: Callable[[Dependencies], QueryHandler],
    ) -> None:
        self._handlers_factory[type_query] = handler_factory

    def get_handler_factory(
        self, type_query: QueryType
    ) -> Callable[["QueryHandlerFactory", QueryType], QueryHandler]:
        handler_factory = self._handlers_factory.get(type_query)
        if handler_factory is None:
            raise KeyError(f"Handler factory for {type_query=} not exist")
        return handler_factory

    @lru_cache()
    def get_handler_object(
        self, type_query: QueryType, dependencies: Dependencies | None
    ) -> QueryHandler:
        dependencies = dependencies or {}
        handler_factory = self.get_handler_factory(type_query)
        handler_object = handler_factory(dependencies)
        return handler_object

    def reset_cache(self) -> None:
        self.get_handler_object.cache_clear()
