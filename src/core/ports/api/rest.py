from abc import abstractmethod
from typing import Protocol
from uuid import UUID

from src.core.cqrs.command import CreateCommand, UpdateCommand
from src.core.cqrs.query import (
    AuthWithPasswordQuery,
    AuthWithRefreshTokenQuery,
    AuthWithUpdateTokenQuery,
)
from src.core.dto import (
    AuthTokenDTO,
    PremissionCreateDTO,
    PremissionDTO,
    RoleCreateDTO,
    RoleDTO,
    UserCreateDTO,
    UserDTO,
    UserFieldEnum,
)


class RestApiUserInterface(Protocol):
    @abstractmethod
    async def create_user(self, command: CreateCommand[UserCreateDTO]):
        pass

    @abstractmethod
    async def delete_user(self, user_id: UUID):
        pass

    @abstractmethod
    async def update_user(self, command: UpdateCommand[UserDTO]):
        pass

    @abstractmethod
    async def get_user_by_id(
        self, user_id: UUID, dto_output: set[UserFieldEnum]
    ) -> UserDTO:
        pass

    @abstractmethod
    async def get_user_by_email(
        self, user_name: str, dto_output: set[UserFieldEnum]
    ) -> UserDTO:
        pass


class RestApiRoleInterface(Protocol):
    @abstractmethod
    async def create_role(self, command: CreateCommand[RoleCreateDTO]):
        pass

    @abstractmethod
    async def delete_role(self, role_id: int):
        pass

    @abstractmethod
    async def update_role(self, command: UpdateCommand[RoleDTO]):
        pass

    @abstractmethod
    async def get_role_by_id(
        self, role_id: int, dto_output: set[str]
    ) -> RoleDTO:
        pass

    @abstractmethod
    async def get_role_by_name(
        self, role_name: str, dto_output: set[str]
    ) -> RoleDTO:
        pass


class RestApiPremissionInterface(Protocol):
    @abstractmethod
    async def create_premission(
        self, command: CreateCommand[PremissionCreateDTO]
    ):
        pass

    @abstractmethod
    async def delete_premission(self, premission_id: int):
        pass

    @abstractmethod
    async def update_premission(self, command: UpdateCommand[PremissionDTO]):
        pass

    @abstractmethod
    async def get_premission_by_id(
        self, premission_id: int, dto_output: set[str]
    ) -> PremissionDTO:
        pass

    @abstractmethod
    async def get_premission_by_name(
        self, premission_name: str, dto_output: set[str]
    ) -> PremissionDTO:
        pass


class RestApiAuthInterface(Protocol):
    @abstractmethod
    async def auth_with_password(
        self, query: AuthWithPasswordQuery
    ) -> AuthTokenDTO:
        pass

    @abstractmethod
    async def auth_with_refresh_token(
        self, query: AuthWithRefreshTokenQuery
    ) -> AuthTokenDTO:
        pass

    @abstractmethod
    async def auth_with_update(
        self, query: AuthWithUpdateTokenQuery
    ) -> AuthTokenDTO:
        pass
