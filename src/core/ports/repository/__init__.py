from .repository import (
    AioCommandRepository,
    AioQueryRepository,
    SyncCommandRepository,
    SyncQueryRepository,
    TIn,
    TOut,
)

type CommandRepositoryType[T] = SyncCommandRepository[T] | AioCommandRepository[T]
type QueryRepositoryType[T] = SyncQueryRepository[T] | AioQueryRepository[T]

__all__ = [
    "QueryRepositoryType",
    "CommandRepositoryType",
    "AioCommandRepository",
    "AioQueryRepository",
    "SyncCommandRepository",
    "SyncQueryRepository",
    "TIn",
    "TOut",
]
