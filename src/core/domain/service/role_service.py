from src.core.domain.entities.aggregates.role_aggragate import RoleAggregate
from src.core.domain.entities.role import Role
from src.core.domain.entities.value_objects import ID
from src.core.ports.repository import CommandRepositoryT, QueryRepositoryType
from src.infrastructure.executor import ExecutorInterface


class RoleService:
    def __init__(
        self,
        role_query_repository: QueryRepositoryType,
        role_command_repository: CommandRepositoryT,
        executor: ExecutorInterface,
    ) -> None:
        self.role_query_repository = role_query_repository
        self.role_command_repository = role_command_repository
        self.executor = executor

    async def get_role_by_id(self, role_id: ID) -> RoleAggregate:
        method = self.role_query_repository.get_by_id
        result = await self.executor.execute(method, role_id)
        return result

    async def get_role_by_name(self, role_name: str) -> RoleAggregate:
        method = self.role_query_repository.get_by_name
        result = await self.executor.execute(method, role_name)
        return result

    async def create_role(self, role_name: str, premission_ids: list[int]):
        method = self.role_command_repository.add
        role_entity = Role(role_name, premission_ids)
        role_aggragate = RoleAggregate(role=role_entity)
        await self.executor.execute(method, role_aggragate)

    async def update_role(self, role_id: ID, role_aggragate: RoleAggregate):
        method = self.role_command_repository.update
        await self.executor.execute(method, role_id, role_aggragate)

    async def delete_role(self, role_id: ID):
        method = self.role_command_repository.delete
        await self.executor.execute(method, role_id)
