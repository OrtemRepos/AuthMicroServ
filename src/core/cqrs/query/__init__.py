from .query import (
    AuthWithPasswordQuery,
    AuthWithRefreshTokenQuery,
    AuthWithUpdateTokenQuery,
    BaseQuery,
    GetByIdQuery,
    GetByNameQuery,
)

type QueryType = (
    GetByIdQuery
    | GetByNameQuery
    | AuthWithPasswordQuery
    | AuthWithUpdateTokenQuery
    | AuthWithRefreshTokenQuery
)

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
