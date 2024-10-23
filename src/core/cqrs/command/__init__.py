from typing import TypeVar

from .command import (
    BaseCommand,
    CreateCommand,
    UpdateCommand,
    DeleteCommand,
)

CommandType = TypeVar("CommandType", bound=BaseCommand, contravariant=True)

__all__ = ["CreateCommand", "UpdateCommand", "DeleteCommand"]
