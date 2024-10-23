from typing import TypeVar, Union

from .authenticate_usecase import (
    BaseAuthUsecaseInterface,
    BaseAuthUsecase,
    AuthUserWithPassword,
    AuthUserWithRefreshToken,
    AuthUserWithUpdateRole,
)
from .user_usecase import (
    BaseUserUsecaseInterface,
    BaseUserUsecase,
    CreateUserUsecase,
    DeleteUserUsecase,
    UpdateUserUsecase,
    GetUserUsecase,
)
from .role_usecase import (
    BaseRoleUsecaseInterface,
    BaseRoleUsecase,
    CreateRoleUsecase,
    DeleteRoleUsecase,
    UpdateRoleUsecase,
    GetRoleUsecase,
)
from .premission_usecase import (
    BasePremissionUsecaseInterface,
    BasePremissionUsecase,
    CreatePremissionUsecase,
    DeletePremissionUsecase,
    UpdatePremissionUsecase,
    GetPremissionUsecase,
)

UsecaseType = TypeVar(
    "UsecaseType",
    bound=Union[
        BasePremissionUsecaseInterface,
        BaseAuthUsecaseInterface,
        BaseUserUsecaseInterface,
        BaseRoleUsecaseInterface,
    ],
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
    "AuthUserWithRefreshToken",
    "AuthUserWithUpdateRole",
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
