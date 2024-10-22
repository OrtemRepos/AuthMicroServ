from typing import TypeVar, Union
from pydantic import BaseModel

from .user import (
    UserBaseIdDTO,
    UserBaseEmailDTO,
    UserBaseRoleDTO,
    UserBasePasswordDTO,
    UserFullDTO,
    UserAuthDTO,
    UserUpdateDTO,
    UserAuthWithTokenDTO,
    UserRefreshTokenDTO,
)

from .role import (
    RoleBaseIdDTO,
    RolePremissionBaseDTO,
    RoleBaseNameDTO,
    RoleFullDTO,
    RoleUpdateDTO,
)

from .premission import (
    PremissionBaseIdDTO,
    PremissionBaseNameDTO,
    PremissionUpdateDTO,
    PremissionFullDTO,
)


UserBaseDTO = TypeVar(
    "UserBaseDTO",
    bound=Union[UserBaseIdDTO, UserBaseEmailDTO, UserBaseRoleDTO, UserBasePasswordDTO],
    covariant=True,
)

RoleBaseDTO = TypeVar(
    "RoleBaseDTO",
    bound=Union[RoleBaseIdDTO, RolePremissionBaseDTO, RoleBaseNameDTO],
    covariant=True,
)

PremissionBaseDTO = TypeVar(
    "PremissionBaseDTO",
    bound=Union[PremissionBaseIdDTO, PremissionBaseNameDTO],
    covariant=True,
)
DTOType = TypeVar("DTOType", bound=BaseModel, covariant=True)

UpdateDTO = TypeVar("UpdateDTO", bound=Union[UserUpdateDTO, RoleUpdateDTO, PremissionUpdateDTO])
IdDTO = TypeVar("IdDTO", bound=Union[UserBaseIdDTO, RoleBaseIdDTO, PremissionBaseIdDTO])
FullDTO = TypeVar("FullDTO", bound=Union[UserFullDTO, RoleFullDTO, PremissionFullDTO])

__all__ = [
    UserBaseIdDTO,
    UserBaseEmailDTO,
    UserBaseRoleDTO,
    UserBasePasswordDTO,
    UserFullDTO,
    UserAuthDTO,
    UserUpdateDTO,
    UserAuthWithTokenDTO,
    UserRefreshTokenDTO,
    UserBaseDTO,
    RoleBaseIdDTO,
    RolePremissionBaseDTO,
    RoleBaseNameDTO,
    RoleFullDTO,
    RoleUpdateDTO,
    RoleBaseDTO,
    PremissionBaseIdDTO,
    PremissionBaseNameDTO,
    PremissionUpdateDTO,
    PremissionFullDTO,
    PremissionBaseDTO,
]
