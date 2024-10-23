from src.core.domain.entities.entity import Entity
from pydantic import Field


class Premission(Entity):
    name: str = Field(
        examples=["only_read", "god_premission"], description="Premission name"
    )
