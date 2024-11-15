from litestar import Controller, Router, delete, get, patch, post

from src.core.cqrs.command.command import (
    CreateCommand,
    DeleteCommand,
    UpdateCommand,
)
from src.core.cqrs.query.query import (
    GetByIdQuery,
    GetByNameQuery,
)
from src.core.dto import RoleCreateDTO, RoleDTO, RoleFieldEnum
from src.infrastructure.facade.client_facade import ClientFacade


class RoleApiLitestar(Controller):
    path = "/"

    def __init__(self, owner: Router, client: ClientFacade) -> None:
        super().__init__(owner)
        self._client = client

    @post(path="/create")
    async def create_user(self, command: CreateCommand[RoleCreateDTO]) -> None:
        await self._client.create(command)

    @delete(path="/delete/{role_id:int}")
    async def delete_user(self, role_id: int) -> None:
        command = DeleteCommand(dto=RoleDTO(role_id=role_id))
        await self._client.delete(command)

    @patch(path="/update")
    async def update_user(self, command: UpdateCommand[RoleDTO]) -> None:
        await self._client.update(command)

    @get(path="/get/{role_id:int}")
    async def get_user_by_id(
        self, role_id: int, dto_output: set[RoleFieldEnum]
    ) -> RoleDTO:
        query = GetByIdQuery(role_id=role_id, dto_output=dto_output)
        return await self._client.get(query)

    @get(path="/get/name/{role_name:str}")
    async def get_user_by_email(
        self, role_name: str, dto_output: set[RoleFieldEnum]
    ) -> RoleDTO:
        query = GetByNameQuery(role_name=role_name, dto_output=dto_output)
        return await self._client.get_by_name(query)
