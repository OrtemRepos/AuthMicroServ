from litestar import Controller, Router

from src.core.cqrs.command.command import (
    CreateCommand,
    DeleteCommand,
    UpdateCommand,
)
from src.core.dto import UserDTO
from src.core.ports.api.rest import RestApiUserInterface
from src.infrastructure.facade.client_facade import ClientFacade


class UserApiLitestar(RestApiUserInterface, Controller):
    path = "/user/"

    def __init__(self, owner: Router, client: ClientFacade) -> None:
        super().__init__(owner)
        self._client = client

    async def create_user(self, command: CreateCommand[UserDTO]) -> None:
        await self._client.create(command)

    async def delete_user(self, command: DeleteCommand[UserDTO]) -> None:
        await self._client.delete(command)

    async def update_user(self, command: UpdateCommand[UserDTO]) -> None:
        await self._client.update(command)

    # async def get_user_by_id(
    #     self, user_id: UUID, dto_output: set[str]
    # ) -> UserDTO:
    #     query = GetByIdQuery[UserDTO](dto=UserDTO(user_id=user_id))
    #     return await self._client.get(query, dto_output)

    # async def get_user_by_email(
    #     self, user_name: str, dto_output: set[str]
    # ) -> UserDTO:
    #     query = GetByNameQuery[UserDTO](
    #         dto=UserDTO(email=user_name)
    #     )
    #     return await self._client.get_by_name(query, dto_output)
