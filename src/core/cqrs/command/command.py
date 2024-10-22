from pydantic import BaseModel, Field

from src.core.dto import UpdateDTO, IdDTO, FullDTO


class BaseCommand(BaseModel):
    name: str = Field(
        examples=["Some-Command-Name"], description="Command name", default=None
    )

    def __init__(self, **data):
        super().__init__(**data)
        if not self.name:
            self.name = self.__class__.__name__


class CreateCommand(BaseCommand):
    dto: FullDTO = Field(description="DTO of new entity")


class UpdateCommand(BaseCommand):
    id: IdDTO
    dto: UpdateDTO


class DeleteCommand(BaseCommand):
    id: IdDTO


class RefreshToken(BaseModel):
    pass
