from abc import ABC

from pydantic import BaseModel, Field

from src.core.dto import CreateDTO, IdDTO, UpdateDTO


class BaseCommand(BaseModel, ABC):
    pass


class CreateCommand(BaseCommand):
    dto: CreateDTO = Field(description="DTO of new entity")


class UpdateCommand(BaseCommand):
    dto: UpdateDTO = Field(description="Updated DTO")


class DeleteCommand(BaseCommand):
    dto: IdDTO = Field(description="DTO with ID entity")
