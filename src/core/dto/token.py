from pydantic import BaseModel
from src.core.domain.entities.value_objects import AccsesToken
from src.core.domain.entities import RefreshToken


class AuthTokenDTO(BaseModel):
    accsess_token: AccsesToken | None = None
    refresh_token: RefreshToken | None = None
