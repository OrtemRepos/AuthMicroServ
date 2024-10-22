from functools import lru_cache, wraps
from typing import Protocol, Callable
from abc import abstractmethod
from src.core.cqrs.command import CommandType
from src.core.ports import Dependencies


class CommandHandler(Protocol[CommandType]):
    @abstractmethod
    async def execute(command: CommandType):
        pass


class CommandHandlerFactory:
    def __init__(self) -> None:
        self._handlers_factory = dict[
            tuple[CommandType, Dependencies], Callable[[Dependencies], CommandHandler]
        ] = {}

    def command_handler(self):
        def decorator(
            func: Callable[[CommandType, Dependencies | None], None],
        ):
            @wraps
            def wrapper(command: CommandType,
                        dependencies: Dependencies,
                        base_class: CommandHandler = CommandHandler):
                class CommandHandlerImpl(base_class[command]):
                    def __init__(
                        self, dependencies: Dependencies | None = dependencies
                    ):
                        self.dependencies = dependencies or {}
                        self.func = func

                    async def execute(self, command: command):
                        return await self.func(command, self.dependencies)

                self.register(
                    command, lambda dependencies: CommandHandlerImpl(dependencies)
                )
                return CommandHandlerImpl

            return wrapper

        return decorator

    def register(
        self,
        type_command: type,
        handler_factory: Callable[[Dependencies], CommandHandler],
    ) -> None:
        self._handlers_factory[type_command] = handler_factory

    def get_handler_factory(
        self, type_command: CommandType
    ) -> type[CommandHandler] | None:
        handler_factory = self._handlers_factory.get(type_command)
        if handler_factory is None:
            raise KeyError(f"Handler factory for {type_command=} not exist")
        return handler_factory

    @lru_cache()
    def get_handler_object(
        self, type_command: CommandType, dependencies: Dependencies | None
    ) -> CommandHandler:
        if dependencies is None:
            dependencies = {}
        from_cache = self._cache.get((type_command, dependencies))
        if from_cache:
            return from_cache
        handler_factory = self.get_handler_factory(type_command)
        handler_object = handler_factory(dependencies)
        self._cache[(type_command, dependencies)] = handler_object
        return handler_object

    def reset_cache(self) -> None:
        self.get_handler_object.cache_clear()
