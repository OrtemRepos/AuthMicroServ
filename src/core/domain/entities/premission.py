from pydantic import Field

from src.core.domain.entities.entity import Entity


class Premission(Entity):
    name: str = Field(
        examples=["only_read", "god_premission"], description="Premission name"
    )
