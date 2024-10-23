from pydantic import BaseModel
from src.core.domain.entities.value_objects import AccsesToken, RefreshToken


class AuthTokenDTO(BaseModel):
    accsess_token: AccsesToken
    refresh_token: RefreshToken
