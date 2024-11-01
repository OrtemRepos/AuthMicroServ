from pydantic import BaseModel

from src.core.domain.entities.value_objects import ID


class Entity(BaseModel):
    id: ID
