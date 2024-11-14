from src.core.cqrs.command.command import (
    CreateCommand,
    DeleteCommand,
    UpdateCommand,
)
from src.core.ports.event_bus import EventBusInterface
from src.infrastructure.query import QueryRouter


class ClientFacade:
    def __init__(
        self, query_router: QueryRouter, command_bus: EventBusInterface
    ):
        self.query_router = query_router
        self.command_bus = command_bus

    async def create(self, command: CreateCommand):
        await self.command_bus.publish(command)

    async def delete(self, command: DeleteCommand):
        await self.command_bus.publish(command)

    async def update(self, command: UpdateCommand):
        await self.command_bus.publish(command)

    # async def get[DTOout: DtoType](
    #     self, command: GetByIdQuery, dto: DTOout
    # ) -> DTOout:
    #     pass

    # async def get_by_name[DTOout: DtoType](
    #     self, command: GetByNameQuery, dto: DTOout
    # ) -> DTOout:
    #     pass
