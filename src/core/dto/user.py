from enum import StrEnum

from pydantic import BaseModel, ConfigDict, EmailStr, Field, SecretStr

from src.core.domain.entities.token_entity import RefreshToken
from src.core.domain.entities.value_objects import ID, AccsesToken


class UserDTO(BaseModel):
    user_id: ID | None = Field(
        default=None, description="User ID (UUID by default)"
    )
    email: EmailStr | None = None
    role_ids: set[int] | None = None
    hashed_password: str | None = None

    model_config = ConfigDict(from_attributes=True, extra="ignore")


class UserCreateDTO(BaseModel):
    email: EmailStr
    password: SecretStr


class UserFieldEnum(StrEnum):
    USER_ID = "user_id"
    EMAIL = "email"
    ROLE_IDS = "role_ids"
    HASHED_PASSWORD = "hashed_password"


class UserAuthDTO(BaseModel):
    email: EmailStr
    password: SecretStr
    aud: str


class UserAuthTokenDTO(BaseModel):
    user_id: ID
    accses_token: AccsesToken
    refresh_token: RefreshToken | None


class UserRefreshTokenUpdatedDTO(BaseModel):
    user_id: ID
    refresh_token: RefreshToken
    aud: str
