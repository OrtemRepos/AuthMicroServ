from pydantic import BaseModel, ConfigDict


class PremissionDTO(BaseModel):
    premission_id: int
    name: str | None = None

    model_config = ConfigDict(from_attributes=True, extra="ignore")
