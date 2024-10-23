from pydantic import BaseModel


class RoleBaseIdDTO(BaseModel):
    role_id: int


class RolePremissionBaseDTO(BaseModel):
    premission_ids: set[int]


class RoleBaseNameDTO(BaseModel):
    name: str


class RoleFullDTO(RoleBaseIdDTO, RolePremissionBaseDTO, RoleBaseNameDTO):
    pass


class RoleUpdateDTO(RolePremissionBaseDTO, RoleBaseNameDTO):
    pass
