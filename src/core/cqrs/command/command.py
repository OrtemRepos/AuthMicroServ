from pydantic import BaseModel, Field
from typing import TypeVar, Generic
from abc import ABC

from src.core.dto import UpdateDTO, IdDTO, CreateDTO

CreateT = TypeVar("CreateT", bound=CreateDTO)
UpdateT = TypeVar("UpdateT", bound=UpdateDTO)
DeleteT = TypeVar("DeleteT", bound=IdDTO)


class BaseCommand(BaseModel, ABC):
    pass


class CreateCommand(BaseCommand, Generic[CreateT]):
    dto: CreateT = Field(description="DTO of new entity")


class UpdateCommand(BaseCommand, Generic[UpdateT]):
    dto: UpdateT


class DeleteCommand(BaseCommand, Generic[DeleteT]):
    dto: DeleteT
