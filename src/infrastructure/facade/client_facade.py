from src.core.cqrs.command.command import (
    CreateCommand,
    DeleteCommand,
    UpdateCommand,
)
from src.core.cqrs.query.query import (
    GetByIdQuery,
    GetByNameQuery,
)
from src.core.dto import TypeDTO
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

    async def get[DTO: (TypeDTO)](
        self, query: GetByIdQuery, dto_output: set[str] | None = None
    ) -> DTO:
        dto: DTO = await self.query_router.execute(query)
        data = dto.model_dump(include=dto_output)
        data = {**data}
        result_dto: DTO = dto.model_validate(data)  # type: ignore
        return result_dto

    async def get_by_name[DTO: (TypeDTO)](
        self, query: GetByNameQuery, dto_output: set[str] | None = None
    ) -> DTO:
        dto: DTO = await self.query_router.execute(query)
        data = dto.model_dump(include=dto_output)
        data = {**data}
        result_dto: DTO = dto.model_validate(data)  # type: ignore
        return result_dto
