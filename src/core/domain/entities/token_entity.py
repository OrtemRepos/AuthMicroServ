import secrets

from pydantic import Field

from src.config import JWTsettings
from src.core.domain.entities.entity import Entity


class RefreshToken(Entity):
    token: str = Field(
        default_factory=lambda: secrets.token_urlsafe(
            JWTsettings().refresh_token_size
        )
    )
