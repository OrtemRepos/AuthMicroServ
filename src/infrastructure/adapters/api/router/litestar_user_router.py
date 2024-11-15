from uuid import UUID

from litestar import Controller, Router, delete, get, patch, post
from pydantic import EmailStr

from src.core.cqrs.command.command import (
    CreateCommand,
    DeleteCommand,
    UpdateCommand,
)
from src.core.cqrs.query.query import (
    GetByIdQuery,
    GetByNameQuery,
)
from src.core.dto import UserCreateDTO, UserDTO, UserFieldEnum
from src.infrastructure.facade.client_facade import ClientFacade


class UserApiLitestar(Controller):
    path = "/"

    def __init__(self, owner: Router, client: ClientFacade) -> None:
        super().__init__(owner)
        self._client = client

    @post(path="/create")
    async def create_user(self, command: CreateCommand[UserCreateDTO]) -> None:
        await self._client.create(command)

    @delete(path="/delete/{user_id:uuid}")
    async def delete_user(self, user_id: UUID) -> None:
        command = DeleteCommand(dto=UserDTO(user_id=user_id))
        await self._client.delete(command)

    @patch(path="/update")
    async def update_user(self, command: UpdateCommand[UserDTO]) -> None:
        await self._client.update(command)

    @get(path="/get/{user_id:uuid}")
    async def get_user_by_id(
        self, user_id: UUID, dto_output: set[UserFieldEnum]
    ) -> UserDTO:
        query = GetByIdQuery[UserDTO](dto=UserDTO(user_id=user_id))
        dto_fields = {str(field) for field in dto_output}
        return await self._client.get(query, dto_fields)

    @get(path="/get/email/{user_name:str}")
    async def get_user_by_email(
        self, user_name: EmailStr, dto_output: set[UserFieldEnum]
    ) -> UserDTO:
        query = GetByNameQuery[UserDTO](dto=UserDTO(email=user_name))
        dto_fields = {str(field) for field in dto_output}
        return await self._client.get_by_name(query, dto_fields)
