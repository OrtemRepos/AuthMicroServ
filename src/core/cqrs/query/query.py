from pydantic import BaseModel, Field
from src.core.domain.entities.value_objects import ID, AccsesToken


class BaseQuery(BaseModel):
    name: str = Field(
        examples=["SomeQueryName"], description="Query name", default=None
    )

    def __init__(self, **data):
        super().__init__(**data)
        if not self.name:
            self.name = self.__class__.__name__


class GetByIdQuery(BaseQuery):
    id: ID


class GetByNameQuery(BaseQuery):
    name: str


class CheckAccsesTokenQuery(BaseQuery):
    token: AccsesToken


class CheckRoleQuery(BaseQuery):
    user_id: ID
    role_id: int


class CheckPremissionQuery(BaseQuery):
    role_id: ID
    premission_id: int
