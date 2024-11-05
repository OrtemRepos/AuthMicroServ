from collections.abc import Callable
from typing import Protocol, TypeVar, get_type_hints

from pydantic import BaseModel

from src.core.cqrs.command import CommandType

TDto = TypeVar("TDto", bound=BaseModel, contravariant=True)


class Handler(Protocol[TDto]):
    def __call__(self, dto: TDto) -> None:
        pass


type HandlerFuncType[TDto] = Callable[[TDto], None] | Handler[TDto]


class CommandRouter:
    def __init__(
        self,
        handlers: dict[type[CommandType], list[HandlerFuncType]] | None = None,
    ) -> None:
        self._handlers: dict[type[CommandType], list[HandlerFuncType]] = (
            {} or handlers
        )

    def register(
        self,
        handle_command: type[CommandType],
        handlers: list[HandlerFuncType[TDto]],
    ) -> bool:
        if handle_command not in self._handlers:
            self._handlers[handle_command] = []
        elif handlers in self._handlers[handle_command]:
            return False
        self._handlers[handle_command].extend(handlers)
        return True

    @staticmethod
    def check_type(
        command: CommandType, handler: HandlerFuncType[TDto]
    ) -> bool:
        command_items = command.__dict__

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
                if isinstance(command_items[k], v):
                    continue
            except KeyError as exc:
                raise TypeError(
                    "Command dont have requires dto.\n"
                    f"DTO requires: \n\t{usecase_type_hints.values()}"
                    f"DTO got: \n\t{list(map(type, command_items.values()))}"
                ) from exc
            return False
        return True

    async def execute(self, command: CommandType) -> None:
        handlers = self._handlers.get(type(command))
        if handlers is None:
            raise TypeError(
                f"Not supporting command {command=}.\n"
                f"Supporting types: \n\t{self._handlers.keys()}"
            )
        for handler in handlers:
            if self.check_type(command, handler):
                handler(command.dto)
        raise TypeError(
            f"Command {command.__class__.__name__} have unsupporting DTO type."
        )
