from abc import ABC
from typing import Generic, TypeVar

from pydantic import BaseModel, Field

from src.core.dto import TypeCreateDTO, TypeDTO

OutDTO = TypeVar("OutDTO", bound=TypeDTO)
CreateDTO = TypeVar("CreateDTO", bound=TypeCreateDTO)


class BaseCommand(BaseModel, ABC):
    pass


class CreateCommand(BaseCommand, Generic[CreateDTO]):
    dto: CreateDTO = Field(description="DTO of new entity")


class UpdateCommand(BaseCommand, Generic[OutDTO]):
    dto: OutDTO = Field(description="Updated DTO")


class DeleteCommand(BaseCommand, Generic[OutDTO]):
    dto: OutDTO = Field(description="DTO with ID entity")
