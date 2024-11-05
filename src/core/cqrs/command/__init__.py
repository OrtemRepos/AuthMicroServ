from .command import (
    CreateCommand,
    DeleteCommand,
    UpdateCommand,
)

type CommandType = CreateCommand | UpdateCommand | DeleteCommand

__all__ = ["CreateCommand", "UpdateCommand", "DeleteCommand"]
