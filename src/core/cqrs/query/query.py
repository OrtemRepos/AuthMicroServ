from abc import ABC

from pydantic import BaseModel

from src.core.dto import (
    AuthTokenDTO,
    TypeDTO,
    UserAuthDTO,
    UserRefreshTokenUpdatedDTO,
)


class BaseQuery(BaseModel, ABC):
    pass


class GetByIdQuery[IdType: TypeDTO](BaseQuery):
    dto: IdType

    def __init__(self, **data):
        super().__init__(**data)

        for key in self.dto.model_fields:
            if "id" in key:
                break
            raise ValueError("Id not found")


class GetByNameQuery[NameType: TypeDTO](BaseQuery):
    dto: NameType


class AuthWithPasswordQuery(BaseQuery):
    dto: UserAuthDTO


class AuthWithRefreshTokenQuery(BaseQuery):
    dto: AuthTokenDTO


class AuthWithUpdateTokenQuery(BaseQuery):
    dto: UserRefreshTokenUpdatedDTO
