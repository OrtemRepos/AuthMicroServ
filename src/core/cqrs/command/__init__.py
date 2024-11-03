from .command import (
    CreateCommand,
    UpdateCommand,
    DeleteCommand,
)

type CommandType = CreateCommand | UpdateCommand | DeleteCommand

__all__ = ["CreateCommand", "UpdateCommand", "DeleteCommand"]
