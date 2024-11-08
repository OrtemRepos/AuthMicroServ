from litestar import Router
from litestar.controller import Controller

from src.core.cqrs.command.command import (
    CreateCommand,
    DeleteCommand,
    UpdateCommand,
)
from src.core.cqrs.query.query import GetByIdQuery
from src.core.ports.api.rest import RestApiUserInterface
from src.core.ports.event_bus import EventBusInterface


class UserRouter(RestApiUserInterface, Controller):
    path = "/user"

    def __init__(self, owner: Router, event_bus: EventBusInterface) -> None:
        super().__init__(owner)
        self._event_bus = event_bus

    async def create_user(self, command: CreateCommand) -> None:
        await self._event_bus.publish(command)

    async def delete_user(self, command: DeleteCommand):
        await self._event_bus.publish(command)

    async def update_user(self, command: UpdateCommand):
        await self._event_bus.publish(command)

    async def get_user_by_id[UserFullDTO](
        self, query: GetByIdQuery
    ) -> UserFullDTO:
        result = await self._event_bus.publish(query)
        return result
