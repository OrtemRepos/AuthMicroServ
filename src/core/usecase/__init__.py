from collections.abc import Callable
from typing import TypeVar

from .authenticate_usecase import (
    AuthUserWithPassword,
    AuthUserWithRefreshTokenUsecase,
    AuthUserWithUpdateRoleUsecase,
    BaseAuthUsecase,
)
from .premission_usecase import (
    BasePremissionUsecase,
    CreatePremissionUsecase,
    DeletePremissionUsecase,
    GetPremissionUsecase,
    UpdatePremissionUsecase,
)
from .role_usecase import (
    BaseRoleUsecase,
    CreateRoleUsecase,
    DeleteRoleUsecase,
    GetRoleUsecase,
    UpdateRoleUsecase,
)
from .user_usecase import (
    BaseUserUsecase,
    CreateUserUsecase,
    DeleteUserUsecase,
    GetUserUsecase,
    UpdateUserUsecase,
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
