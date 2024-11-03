from typing import Union

from .query import (
    BaseQuery,
    GetByIdQuery,
    GetByNameQuery,
    AuthWithPasswordQuery,
    AuthWithUpdateTokenQuery,
    AuthWithRefreshTokenQuery,
)

type QueryType = Union[
    GetByIdQuery,
    GetByNameQuery,
    AuthWithPasswordQuery,
    AuthWithUpdateTokenQuery,
    AuthWithRefreshTokenQuery,
]

__all__ = [
    "BaseQuery",
    "GetByIdQuery",
    "GetByNameQuery",
    "CheckAccsesTokenQuery",
    "CheckPremissionQuery",
    "CheckRoleQuery",
    "AuthWithPasswordQuery",
    "AuthWithUpdateTokenQuery",
    "AuthWithRefreshTokenQuery",
]
