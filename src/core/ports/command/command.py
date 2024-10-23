from functools import lru_cache, wraps
from typing import Protocol, Callable
from abc import abstractmethod
from src.core.usecase import UsecaseType
from src.core.cqrs.command import CommandType


type Dependency = tuple[CommandType, UsecaseType]  # type: ignore


class CommandHandler(Protocol[CommandType]):
    @abstractmethod
    async def execute(self, command: CommandType, usecase: UsecaseType) -> None:
        pass


class CommandHandlerRouter:
    def __init__(self) -> None:
        self._handlers_factory: dict[Dependency, type[CommandHandler]] = {}

    def command_handler(self, base_class: type[CommandHandler] = CommandHandler):
        def decorator(
            func: Callable[
                [CommandType, UsecaseType],
                None,
            ],
        ):
            @wraps(func)
            def wrapper(
                command_type: CommandType, usecase_type: UsecaseType
            ) -> type[CommandHandler]:
                class CommandHandlerImpl(base_class[command_type]):  # type: ignore
                    def __init__(self, *args, **kwargs):
                        super().__init__(*args, **kwargs)

                    async def execute(
                        self,
                        command: command_type,  # type: ignore
                        usecase: usecase_type,  # type: ignore
                    ) -> None:
                        func(command, usecase)

                return CommandHandlerImpl

            self._register(
                (
                    wrapper.__annotations__["command_type"],
                    wrapper.__annotations__["usecase_type"],
                ),
                wrapper(
                    wrapper.__annotations__["command_type"],
                    wrapper.__annotations__["usecase_type"],
                ),
            )
            return wrapper

        return decorator

    def _register(
        self,
        dependency: Dependency,
        handler_class: type[CommandHandler],
    ) -> None:
        self._handlers_factory[dependency] = handler_class

    def get_handler_class(self, dependency: Dependency) -> type[CommandHandler]:
        handler_class = self._handlers_factory.get(dependency)
        if handler_class is None:
            raise KeyError(f"Handler factory for {dependency=} not exist")
        return handler_class

    @lru_cache()
    def get_handler_object(
        self, dependency: Dependency, *args, **kwargs
    ) -> CommandHandler:
        handler_class = self.get_handler_class(dependency)
        handler_object = handler_class(*args, **kwargs)
        return handler_object

    def reset_cache(self) -> None:
        self.get_handler_object.cache_clear()
