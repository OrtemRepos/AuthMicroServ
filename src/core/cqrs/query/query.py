from abc import ABC
from pydantic import BaseModel
from typing import TypeVar, Generic
from src.core.dto import (
    NameDTO,
    IdDTO,
    UserAuthDTO,
    AuthTokenDTO,
    UserRefreshTokenUpdatedDTO,
)

NameT = TypeVar("NameT", bound=NameDTO)
IdT = TypeVar("IdT", bound=IdDTO)


class BaseQuery(BaseModel, ABC):
    pass


class GetByIdQuery(BaseQuery, Generic[IdT]):
    dto: IdT


class GetByNameQuery(BaseQuery, Generic[NameT]):
    dto: NameT


class AuthWithPasswordQuery(BaseQuery):
    dto: UserAuthDTO


class AuthWithRefreshTokenQuery(BaseQuery):
    dto: AuthTokenDTO


class AuthWithUpdateTokenQuery(BaseQuery):
    dto: UserRefreshTokenUpdatedDTO
