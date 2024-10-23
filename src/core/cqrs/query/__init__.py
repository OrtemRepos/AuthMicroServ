from typing import TypeVar

from .query import (
    BaseQuery,
    GetByIdQuery,
    GetByNameQuery,
    CheckAccsesTokenQuery,
    CheckPremissionQuery,
    CheckRoleQuery,
)

QueryType = TypeVar("QueryType", bound=BaseQuery, contravariant=True)

__all__ = [
    "BaseQuery",
    "GetByIdQuery",
    "GetByNameQuery",
    "CheckAccsesTokenQuery",
    "CheckPremissionQuery",
    "CheckRoleQuery",
]
