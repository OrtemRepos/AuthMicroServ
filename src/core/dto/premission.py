from pydantic import BaseModel


class PremissionBaseIdDTO(BaseModel):
    premission_id: int


class PremissionBaseNameDTO(BaseModel):
    name: str


class PremissionUpdateDTO(PremissionBaseNameDTO):
    pass


class PremissionFullDTO(PremissionBaseIdDTO, PremissionBaseNameDTO):
    pass


class PremissionCreateDTO(PremissionBaseNameDTO):
    pass
