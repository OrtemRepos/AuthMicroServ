from pydantic import BaseModel

from src.core.domain.entities.value_objects import ID


class RoleBaseIdDTO(BaseModel):
    role_id: ID


class RolePremissionBaseDTO(BaseModel):
    premission_ids: set[ID]


class RoleBaseNameDTO(BaseModel):
    name: str


class RoleFullDTO(RoleBaseIdDTO, RolePremissionBaseDTO, RoleBaseNameDTO):
    pass


class RoleUpdateDTO(RolePremissionBaseDTO, RoleBaseNameDTO):
    pass
