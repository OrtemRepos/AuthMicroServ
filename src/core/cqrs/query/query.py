from abc import ABC
from pydantic import BaseModel
from src.core.dto import (
    NameDTO,
    IdDTO,
    UserAuthDTO,
    AuthTokenDTO,
    UserRefreshTokenUpdatedDTO,
)


class BaseQuery(BaseModel, ABC):
    pass


class GetByIdQuery(BaseQuery):
    dto: IdDTO


class GetByNameQuery(BaseQuery):
    dto: NameDTO


class AuthWithPasswordQuery(BaseQuery):
    dto: UserAuthDTO


class AuthWithRefreshTokenQuery(BaseQuery):
    dto: AuthTokenDTO


class AuthWithUpdateTokenQuery(BaseQuery):
    dto: UserRefreshTokenUpdatedDTO
