from pydantic import Field
import secrets
from src.core.domain.entities.entity import Entity
from src.config import JWTsettings


class RefreshToken(Entity):
    token: str = Field(
        default_factory=lambda: secrets.token_urlsafe(JWTsettings().refresh_token_size)
    )
