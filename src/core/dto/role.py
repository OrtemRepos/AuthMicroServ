from pydantic import BaseModel, ConfigDict


class RoleDTO(BaseModel):
    role_id: int
    name: str
    premission_ids: set[int] | None = None

    model_config = ConfigDict(from_attributes=True, extra="ignore")
