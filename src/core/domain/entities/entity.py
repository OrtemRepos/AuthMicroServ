from src.core.domain.entities.value_objects import ID
from pydantic import BaseModel


class Entity(BaseModel):
    id: ID
