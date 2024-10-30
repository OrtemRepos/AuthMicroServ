from typing import TypeVar
from collections.abc import Callable

from .authenticate_usecase import (
    BaseAuthUsecase,
    AuthUserWithPassword,
    AuthUserWithRefreshTokenUsecase,
    AuthUserWithUpdateRoleUsecase,
)
from .user_usecase import (
    BaseUserUsecase,
    CreateUserUsecase,
    DeleteUserUsecase,
    UpdateUserUsecase,
    GetUserUsecase,
)
from .role_usecase import (
    BaseRoleUsecase,
    CreateRoleUsecase,
    DeleteRoleUsecase,
    UpdateRoleUsecase,
    GetRoleUsecase,
)
from .premission_usecase import (
    BasePremissionUsecase,
    CreatePremissionUsecase,
    DeletePremissionUsecase,
    UpdatePremissionUsecase,
    GetPremissionUsecase,
)

UsecaseType = TypeVar(
    "UsecaseType",
    bound=Callable,
    contravariant=True,
)

AuthenticateUsecase = TypeVar(
    "AuthenticateUsecase", bound=BaseAuthUsecase, covariant=True
)
UserUsecase = TypeVar("UserUsecase", bound=BaseUserUsecase, covariant=True)
RoleUsecase = TypeVar("RoleUsecase", bound=BaseRoleUsecase, covariant=True)
PremissionUsecase = TypeVar(
    "PremissionUsecase", bound=BasePremissionUsecase, covariant=True
)


__all__ = [
    "BaseAuthUsecase",
    "AuthUserWithPassword",
    "AuthUserWithRefreshTokenUsecase",
    "AuthUserWithUpdateRoleUsecase",
    "AuthenticateUsecase",
    "BaseUserUsecase",
    "CreateUserUsecase",
    "DeleteUserUsecase",
    "UpdateUserUsecase",
    "GetUserUsecase",
    "UserUsecase",
    "BaseRoleUsecase",
    "CreateRoleUsecase",
    "DeleteRoleUsecase",
    "UpdateRoleUsecase",
    "GetRoleUsecase",
    "RoleUsecase",
    "BasePremissionUsecase",
    "CreatePremissionUsecase",
    "DeletePremissionUsecase",
    "UpdatePremissionUsecase",
    "GetPremissionUsecase",
    "PremissionUsecase",
]
