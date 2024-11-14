from abc import ABC
from typing import Generic, TypeVar

from pydantic import BaseModel, Field

from src.core.dto import DtoType

DTO = TypeVar("DTO", bound=DtoType)


class BaseCommand(BaseModel, ABC):
    pass


class CreateCommand(BaseCommand, Generic[DTO]):
    dto: DTO = Field(description="DTO of new entity")


class UpdateCommand(BaseCommand, Generic[DTO]):
    dto: DTO = Field(description="Updated DTO")


class DeleteCommand(BaseCommand, Generic[DTO]):
    dto: DTO = Field(description="DTO with ID entity")
