from typing import TypeVar
from pydantic import BaseModel

from .user import (
    UserBaseIdDTO,
    UserBaseEmailDTO,
    UserBaseRoleDTO,
    UserBasePasswordDTO,
    UserAuthDTO,
    UserUpdateDTO,
    UserAuthWithTokenDTO,
    UserRefreshTokenDTO,
    UserFullDTO,
    UserRefreshTokenUpdatedDTO,
)

from .role import (
    RoleBaseIdDTO,
    RolePremissionBaseDTO,
    RoleBaseNameDTO,
    RoleUpdateDTO,
    RoleFullDTO,
    RoleCreateDTO,
)

from .premission import (
    PremissionBaseIdDTO,
    PremissionBaseNameDTO,
    PremissionUpdateDTO,
    PremissionFullDTO,
    PremissionCreateDTO,
)

from .token import AuthTokenDTO


DTOTypeCovariant = TypeVar("DTOTypeCovariant", bound=BaseModel, covariant=True)

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
