from typing import Any, Protocol
from src.core.cqrs.command import CommandType
from src.core.cqrs.query import QueryType

type UsecaseHandler = dict[dict[str, Any], dict[str, Any]]


class UsecaseRouterInterface(Protocol):
    usecase_handle_command: UsecaseHandler
    usecase_handle_query: UsecaseHandler

    def __init__(self, usecase_handle: UsecaseHandler) -> None:
        pass

    def get_usecase(self, command_or_handler: CommandType | QueryType) -> Any:
        pass


class UsecaseRouter(UsecaseRouterInterface):
    @staticmethod
    def check_type(command: CommandType | QueryType, usecase: Any):
        command_items = command.__dict__

        usecase_annotations = usecase.__call__.__annotations__
        usecase_annotations.pop("return")
        for k, v in usecase_annotations.items():
            if isinstance(command_items[k], v):
                continue
            return False
        return True
