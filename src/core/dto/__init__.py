from .premission import PremissionCreateDTO, PremissionDTO
from .role import RoleCreateDTO, RoleDTO, RoleFieldEnum
from .token_dto import AuthTokenDTO
from .user import (
    UserAuthDTO,
    UserAuthTokenDTO,
    UserCreateDTO,
    UserDTO,
    UserFieldEnum,
    UserRefreshTokenUpdatedDTO,
)

type TypeCreateDTO = PremissionCreateDTO | RoleCreateDTO | UserCreateDTO
type TypeDTO = UserDTO | RoleDTO | PremissionDTO
type AuthDTO = (
    UserAuthDTO | UserAuthTokenDTO | UserRefreshTokenUpdatedDTO | AuthTokenDTO
)

__all__ = [
    "UserDTO",
    "UserAuthDTO",
    "UserAuthTokenDTO",
    "UserCreateDTO",
    "UserRefreshTokenUpdatedDTO",
    "RoleDTO",
    "PremissionDTO",
    "AuthTokenDTO",
    "UserFieldEnum",
    "RoleFieldEnum",
]
