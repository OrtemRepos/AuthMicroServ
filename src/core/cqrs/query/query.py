from abc import ABC

from pydantic import BaseModel

from src.core.dto import (
    AuthTokenDTO,
    DtoType,
    UserAuthDTO,
    UserRefreshTokenUpdatedDTO,
)


class BaseQuery(BaseModel, ABC):
    pass


class GetByIdQuery[IdType: DtoType](BaseQuery):
    dto: IdType

    def __init__(self, **data):
        super().__init__(**data)

        for key in self.dto.model_fields:
            if "id" in key:
                break
            raise ValueError("Id not found")


class GetByNameQuery[NameType: DtoType](BaseQuery):
    dto: NameType


class AuthWithPasswordQuery(BaseQuery):
    dto: UserAuthDTO


class AuthWithRefreshTokenQuery(BaseQuery):
    dto: AuthTokenDTO


class AuthWithUpdateTokenQuery(BaseQuery):
    dto: UserRefreshTokenUpdatedDTO
