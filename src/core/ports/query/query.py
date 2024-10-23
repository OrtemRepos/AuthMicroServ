from functools import lru_cache, wraps
from typing import Any, Protocol, Callable
from abc import abstractmethod
from src.core.usecase import UsecaseType
from src.core.cqrs.query import QueryType

Dependency = tuple[QueryType, UsecaseType]  # type: ignore


class QueryHandler(Protocol[QueryType]):
    @abstractmethod
    async def execute(self, query: QueryType, usecase: Any):
        pass


class QueryHandlerRouter:
    def __init__(self) -> None:
        self._handlers_factory: dict[Dependency, type[QueryHandler]] = {}

    def query_handler(self, base_class: QueryHandler = QueryHandler):  # type: ignore
        def decorator(
            func: Callable[
                [QueryType, UsecaseType],
                Any,
            ],
        ):
            @wraps(func)
            def wrapper(query_type: QueryType, usecase_type: Any):
                class QueryHandlerImpl(base_class[query_type]):  # type: ignore
                    def __init__(self, *args, **kwargs):
                        super().__init__(*args, **kwargs)

                    async def execute(
                        self,
                        query: query_type,  # type: ignore
                        usecase: usecase_type,  # type: ignore
                    ):
                        return await func(query, usecase)

                return QueryHandlerImpl

            self._register(
                (
                    wrapper.__annotations__["query_type"],
                    wrapper.__annotations__["usecase_type"],
                ),
                wrapper(
                    wrapper.__annotations__["query_type"],
                    wrapper.__annotations__["usecase_type"],
                ),
            )
            return wrapper

        return decorator

    def _register(
        self,
        dependency: Dependency,
        handler_class: type[QueryHandler],
    ) -> None:
        self._handlers_factory[dependency] = handler_class

    def get_handler_class(self, dependency: Dependency) -> type[QueryHandler]:
        handler_class = self._handlers_factory.get(dependency)
        if handler_class is None:
            raise KeyError(f"Handler factory for {dependency=} not exist")
        return handler_class

    @lru_cache()
    def get_handler_object(
        self, dependency: Dependency, *args, **kwargs
    ) -> QueryHandler:
        handler_class = self.get_handler_class(dependency)
        handler_object = handler_class(*args, **kwargs)
        return handler_object

    def reset_cache(self) -> None:
        self.get_handler_object.cache_clear()
