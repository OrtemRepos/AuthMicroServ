from .premission import PremissionDTO
from .role import RoleDTO
from .token_dto import AuthTokenDTO
from .user import (
    UserAuthDTO,
    UserAuthTokenDTO,
    UserDTO,
    UserFieldEnum,
    UserRefreshTokenUpdatedDTO,
)

type DtoType = UserDTO | RoleDTO | PremissionDTO
type AuthDTO = (
    UserAuthDTO | UserAuthTokenDTO | UserRefreshTokenUpdatedDTO | AuthTokenDTO
)

__all__ = [
    "UserDTO",
    "UserAuthDTO",
    "UserAuthTokenDTO",
    "UserRefreshTokenUpdatedDTO",
    "RoleDTO",
    "PremissionDTO",
    "AuthTokenDTO",
    "UserFieldEnum",
]
