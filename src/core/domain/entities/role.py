from pydantic import Field

from src.core.domain.entities.entity import Entity


class Role(Entity):
    name: str = Field(examples=["admin", "user"], description="Role name")
    permission_ids: set[int] = Field(
        examples=[1, 2, 3], description="List of permission ids"
    )
