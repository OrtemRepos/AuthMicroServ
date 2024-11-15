from enum import StrEnum

from pydantic import BaseModel, ConfigDict


class RoleDTO(BaseModel):
    role_id: int | None
    name: str | None
    premission_ids: set[int] | None = None

    model_config = ConfigDict(from_attributes=True, extra="ignore")


class RoleCreateDTO(BaseModel):
    name: str
    premission_ids: set[int]


class RoleFieldEnum(StrEnum):
    role_id = "role_id"
    name = "name"
    premission_ids = "premission_ids"
