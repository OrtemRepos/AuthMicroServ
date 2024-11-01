from .premission import (
    PremissionBaseIdDTO,
    PremissionBaseNameDTO,
    PremissionCreateDTO,
    PremissionFullDTO,
    PremissionUpdateDTO,
)
from .role import (
    RoleBaseIdDTO,
    RoleBaseNameDTO,
    RoleCreateDTO,
    RoleFullDTO,
    RolePremissionBaseDTO,
    RoleUpdateDTO,
)
from .token_dto import AuthTokenDTO
from .user import (
    UserAuthDTO,
    UserAuthWithTokenDTO,
    UserBaseEmailDTO,
    UserBaseIdDTO,
    UserBasePasswordDTO,
    UserBaseRoleDTO,
    UserFullDTO,
    UserRefreshTokenDTO,
    UserRefreshTokenUpdatedDTO,
    UserUpdateDTO,
)

type NameDTO = UserBaseEmailDTO | RoleBaseNameDTO | PremissionBaseNameDTO
type FullDTO = UserFullDTO | RoleFullDTO | PremissionFullDTO
type CreateDTO = UserFullDTO | RoleCreateDTO | PremissionCreateDTO
type IdDTO = UserBaseIdDTO | RoleBaseIdDTO | PremissionBaseIdDTO
type UpdateDTO = UserUpdateDTO | RoleUpdateDTO | PremissionUpdateDTO

__all__ = [
    "UserBaseIdDTO",
    "UserBaseEmailDTO",
    "UserBaseRoleDTO",
    "UserBasePasswordDTO",
    "UserFullDTO",
    "UserAuthDTO",
    "UserUpdateDTO",
    "UserAuthWithTokenDTO",
    "UserRefreshTokenDTO",
    "UserRefreshTokenUpdatedDTO",
    "UserBaseDTO",
    "RoleBaseIdDTO",
    "RolePremissionBaseDTO",
    "RoleBaseNameDTO",
    "RoleFullDTO",
    "RoleUpdateDTO",
    "RoleBaseDTO",
    "PremissionBaseIdDTO",
    "PremissionBaseNameDTO",
    "PremissionUpdateDTO",
    "PremissionFullDTO",
    "PremissionBaseDTO",
    "AuthTokenDTO",
]
