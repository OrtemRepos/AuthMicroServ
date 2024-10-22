from typing import TypeVar

from .query import (
    BaseQuery,
    GetByIdQuery,
    GetByNameQuery,
    CheckAccsesTokenQuery,
    CheckPremissionQuery,
    CheckRoleQuery,
)

QueryType = TypeVar("QueryType", bound=BaseQuery, covariant=True)

__all__ = [
    BaseQuery,
    GetByIdQuery,
    GetByNameQuery,
    CheckAccsesTokenQuery,
    CheckPremissionQuery,
    CheckRoleQuery,
]
