from src.core.domain.entities.aggregates.role_aggragate import RoleAggregate
from src.core.domain.entities.value_objects import ID
from src.core.ports.repository import CommandRepositoryType, QueryRepositoryType
from src.infrastructure.executor import ExecutorInterface


class RoleService:
    def __init__(
        self,
        role_query_repository: QueryRepositoryType,
        role_command_repository: CommandRepositoryType,
        executor: ExecutorInterface,
    ) -> None:
        self.role_query_repository = role_query_repository
        self.role_command_repository = role_command_repository
        self.executor = executor

    async def get_role_by_id(self, role_id: ID) -> RoleAggregate:
        method = self.role_query_repository.get_by_id
        result = await self.executor.execute(method, role_id)
        if result:
            return result
        raise ValueError(f"Not valid {role_id=}")

    async def get_role_by_name(self, role_name: str) -> RoleAggregate:
        method = self.role_query_repository.get_by_name
        result = await self.executor.execute(method, role_name)
        if result:
            return result
        raise ValueError(f"Not valid {role_name=}")

    async def create_role(self, new_role: RoleAggregate) -> None:
        method = self.role_command_repository.add
        await self.executor.execute(method, new_role)

    async def update_role(self, role_aggragate: RoleAggregate) -> None:
        method = self.role_command_repository.update
        await self.executor.execute(method, role_aggragate)

    async def delete_role(self, role_id: ID) -> None:
        method = self.role_command_repository.delete
        await self.executor.execute(method, role_id)
