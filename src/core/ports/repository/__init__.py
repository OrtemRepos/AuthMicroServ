from typing import TypeVar
from .repository import (
    AioCommandRepository,
    AioQueryRepository,
    SyncCommandRepository,
    SyncQueryRepository,
)

CommandRepositoryType = TypeVar(
    "CommandRepositoryType", bound=SyncCommandRepository | AioCommandRepository
)
QueryRepositoryType = TypeVar(
    "QueryRepositoryType", bound=SyncQueryRepository | AioQueryRepository
)

__all__ = [
    QueryRepositoryType,
    CommandRepositoryType,
    AioCommandRepository,
    AioQueryRepository,
    SyncCommandRepository,
    SyncQueryRepository,
]
