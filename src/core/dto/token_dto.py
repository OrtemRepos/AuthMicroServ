from pydantic import BaseModel

from src.core.domain.entities.token_entity import RefreshToken
from src.core.domain.entities.value_objects import AccsesToken


class AuthTokenDTO(BaseModel):
    accsess_token: AccsesToken | None = None
    refresh_token: RefreshToken | None = None
