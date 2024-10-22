from pydantic import BaseModel, EmailStr, Field, SecretStr
from src.core.domain.entities.value_objects import ID, AccsesToken, RefreshToken


class UserBaseIdDTO(BaseModel):
    user_id: ID = Field(description="User ID (UUID by default)")


class UserBaseEmailDTO(BaseModel):
    email: EmailStr


class UserBaseRoleDTO(BaseModel):
    role_ids: set[int] = Field(description="Set with user roles id (int)")


class UserBasePasswordDTO(BaseModel):
    hashed_password: str


class UserFullDTO(
    UserBaseIdDTO, UserBaseEmailDTO, UserBaseRoleDTO, UserBasePasswordDTO
):
    pass


class UserAuthDTO(UserBaseEmailDTO):
    password: SecretStr


class UserUpdateDTO(UserBaseEmailDTO, UserBaseRoleDTO, UserBasePasswordDTO):
    pass


class UserAuthWithTokenDTO(UserBaseIdDTO):
    accses_token: AccsesToken


class UserRefreshTokenDTO(UserBaseIdDTO):
    refresh_token: RefreshToken
