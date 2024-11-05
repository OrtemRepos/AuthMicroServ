from collections.abc import Callable
from typing import Protocol, TypeVar, get_type_hints

from pydantic import BaseModel

from src.core.cqrs.query import QueryType

TDtoInput = TypeVar("TDtoInput", bound=BaseModel, contravariant=True)
TDtoOut = TypeVar("TDtoOut", bound=BaseModel, covariant=True)


class Handler(Protocol[TDtoInput, TDtoOut]):
    def __call__(self, dto: TDtoInput) -> TDtoOut:
        pass


type HandlerFuncType[TDtoInput, TDtoOut] = (
    Callable[[TDtoInput], TDtoOut] | Handler[TDtoInput, TDtoOut]
)


class QueryRouter:
    def __init__(self) -> None:
        self._handlers: dict[type[QueryType], list[HandlerFuncType]] = {}

    def register(
        self,
        handle_query: type[QueryType],
        handlers: list[HandlerFuncType[TDtoInput, TDtoOut]],
    ) -> bool:
        if handle_query not in self._handlers:
            self._handlers[handle_query] = []
        elif handlers in self._handlers[handle_query]:
            return False
        self._handlers[handle_query].extend(handlers)
        return True

    @staticmethod
    def check_type(
        query: QueryType, handler: HandlerFuncType[TDtoInput, TDtoOut]
    ) -> bool:
        query_items = query.__dict__

        if callable(handler):
            usecase_type_hints = get_type_hints(handler)
        elif callable(handler):
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

    async def execute[TDtoOut: BaseModel](
        self, query: QueryType, dto_output
    ) -> TDtoOut:
        handlers = self._handlers.get(type(query))
        if handlers is None:
            raise TypeError(
                f"Not supporting query {query=}.\n"
                f"Supporting types: \n\t{self._handlers.keys()}"
            )
        for handler in handlers:
            if self.check_type(query, handler):
                result: TDtoOut = await handler(query.dto)
                return dto_output.model_validate(result)
        raise TypeError(
            f"Query {query.__class__.__name__} have unsupporting DTO type."
        )
