from src.core.domain.entities import Premission
from src.core.domain.entities.value_objects import ID
from src.core.ports.repository import CommandRepositoryT, QueryRepositoryType
from src.infrastructure.executor import ExecutorInterface


class PremissionService:
    def __init__(
        self,
        premission_query_repository: QueryRepositoryType,
        premission_command_repository: CommandRepositoryT,
        executor: ExecutorInterface,
    ) -> None:
        self.premission_query_repository = premission_query_repository
        self.premission_command_repository = premission_command_repository
        self.executor = executor

    async def get_premission_by_id(self, premission_id: ID) -> Premission:
        method = self.premission_query_repository.get_by_id
        premission = await self.executor.execute(method, premission_id)
        return premission

    async def get_premission_by_name(self, premission_name: str) -> Premission:
        method = self.premission_query_repository.get_by_name
        premission = await self.executor.execute(method, premission_name)
        return premission

    async def add_premission(self, premission: Premission):
        method = self.premission_command_repository.add
        await self.executor.execute(method, premission)

    async def update_premission(self, premission: Premission):
        method = self.premission_command_repository.update
        await self.executor.execute(method, premission)

    async def delete_premisson(self, premission_id: ID):
        method = self.premission_command_repository.delete
        await self.executor.execute(method, premission_id)
