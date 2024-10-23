from pydantic import BaseModel, Field

from typing import Any

from src.core.dto import (
    UserAuthDTO,
    UserAuthWithTokenDTO,
    UserRefreshTokenDTO,
)


class BaseCommand(BaseModel):
    name: str = Field(
        examples=["Some-Command-Name"], description="Command name", default=None
    )

    def __init__(self, **data):
        super().__init__(**data)
        if not self.name:
            self.name = self.__class__.__name__


class CreateCommand(BaseCommand):
    dto: Any = Field(description="DTO of new entity")


class UpdateCommand(BaseCommand):
    id: Any
    dto: Any


class DeleteCommand(BaseCommand):
    id: Any


class AuthWithPasswordCommand(BaseCommand):
    dto: UserAuthDTO


class AuthWithTokenCommand(BaseCommand):
    dto: UserAuthWithTokenDTO


class AuthWithRefreshCommand(BaseCommand):
    dto: UserRefreshTokenDTO
