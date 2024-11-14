from collections.abc import Callable
from typing import Protocol, TypeVar, get_type_hints

from pydantic import BaseModel

from src.core.cqrs.query import QueryType
from src.core.domain.entities.aggregates import DomainEntityType

TDtoInput = TypeVar("TDtoInput", bound=BaseModel, contravariant=True)
EntityType = TypeVar("EntityType", bound=DomainEntityType, covariant=True)


class Handler(Protocol[TDtoInput, EntityType]):
    def __call__(self, dto: TDtoInput) -> EntityType:
        pass


type HandlerFuncType[TDtoInput: BaseModel, EntityType: DomainEntityType] = (
    Callable[[TDtoInput], EntityType] | Handler[TDtoInput, EntityType]
)


class QueryRouter:
    def __init__(self) -> None:
        self._handlers: dict[type[QueryType], list[HandlerFuncType]] = {}

    def register(
        self,
        handle_query: type[QueryType],
        handlers: list[HandlerFuncType[TDtoInput, EntityType]],
    ) -> bool:
        if handle_query not in self._handlers:
            self._handlers[handle_query] = []
        elif handlers in self._handlers[handle_query]:
            return False
        self._handlers[handle_query].extend(handlers)
        return True

    @staticmethod
    def check_type(
        query: QueryType, handler: HandlerFuncType[TDtoInput, EntityType]
    ) -> bool:
        query_items = query.__dict__

        if callable(handler):
            usecase_type_hints = get_type_hints(handler)
        elif isinstance(handler, Handler):
            usecase_type_hints = get_type_hints(handler.__call__)
        else:
            raise TypeError(
                f"Not supporting handler {handler.__class__.__name__}"
            )

        usecase_type_hints.pop("return")

        for k, v in usecase_type_hints.items():
            try:
                if isinstance(query_items[k], v):
                    continue
            except KeyError as exc:
                raise TypeError(
                    "Query dont have requires dto.\n"
                    f"DTO requires: \n\t{usecase_type_hints.values()}"
                    f"DTO got: \n\t{list(map(type, query_items.values()))}"
                ) from exc
            return False
        return True

    async def execute[EntityType: DomainEntityType](
        self, query: QueryType
    ) -> EntityType:
        handlers = self._handlers.get(type(query))
        if handlers is None:
            raise TypeError(
                f"Not supporting query {query=}.\n"
                f"Supporting types: \n\t{self._handlers.keys()}"
            )
        for handler in handlers:
            if self.check_type(query, handler):
                result: EntityType = await handler(query.dto)
                return result
        raise TypeError(
            f"Query {query.__class__.__name__} have unsupporting DTO type."
        )
