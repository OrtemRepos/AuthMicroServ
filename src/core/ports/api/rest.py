from abc import abstractmethod
from typing import Protocol

from pydantic import BaseModel

from src.core.cqrs.command import CreateCommand, DeleteCommand, UpdateCommand
from src.core.cqrs.query import (
    AuthWithPasswordQuery,
    AuthWithRefreshTokenQuery,
    AuthWithUpdateTokenQuery,
    GetByIdQuery,
    GetByNameQuery,
)
from src.core.dto import AuthTokenDTO


class RestApiInterface(Protocol):
    @abstractmethod
    async def create_user(self, command: CreateCommand):
        pass

    @abstractmethod
    async def delete_user(self, command: DeleteCommand):
        pass

    @abstractmethod
    async def update_user(self, command: UpdateCommand):
        pass

    @abstractmethod
    async def get_user_by_id[DTOOut: BaseModel](
        self, query: GetByIdQuery, dto_output: type[DTOOut]
    ) -> DTOOut:
        pass

    @abstractmethod
    async def get_user_by_email[DTOOut: BaseModel](
        self, query: GetByNameQuery, dto_output: type[DTOOut]
    ) -> DTOOut:
        pass

    @abstractmethod
    async def create_role(self, command: CreateCommand):
        pass

    @abstractmethod
    async def delete_role(self, command: DeleteCommand):
        pass

    @abstractmethod
    async def update_role(self, command: UpdateCommand):
        pass

    @abstractmethod
    async def get_role_by_id[DTOOut: BaseModel](
        self, query: GetByIdQuery, dto_output: type[DTOOut]
    ) -> DTOOut:
        pass

    @abstractmethod
    async def get_role_by_name[DTOOut: BaseModel](
        self, query: GetByNameQuery, dto_output: type[DTOOut]
    ) -> DTOOut:
        pass

    @abstractmethod
    async def create_premission(self, command: CreateCommand):
        pass

    @abstractmethod
    async def delete_premission(self, command: DeleteCommand):
        pass

    @abstractmethod
    async def update_premission(self, command: UpdateCommand):
        pass

    @abstractmethod
    async def get_premission_by_id[DTOOut: BaseModel](
        self, query: GetByIdQuery, dto_output: type[DTOOut]
    ) -> DTOOut:
        pass

    @abstractmethod
    async def get_premission_by_name[DTOOut: BaseModel](
        self, query: GetByNameQuery, dto_output: type[DTOOut]
    ) -> DTOOut:
        pass

    @abstractmethod
    async def auth_with_password(self, query: AuthWithPasswordQuery) -> AuthTokenDTO:
        pass

    @abstractmethod
    async def auth_with_refresh_token(
        self, query: AuthWithRefreshTokenQuery
    ) -> AuthTokenDTO:
        pass

    @abstractmethod
    async def auth_with_update(self, query: AuthWithUpdateTokenQuery) -> AuthTokenDTO:
        pass
