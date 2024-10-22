from core.domain.entities.value_objects import ID
from src.core.domain.entities.aggregates.user_aggregate import UserAggregate
from src.core.ports.repository import QueryRepositoryType, CommandRepositoryT
from src.infrastructure.executor import ExecutorInterface


class UserService:
    def __init__(
        self,
        user_query_repository: QueryRepositoryType,
        user_command_repository: CommandRepositoryT,
        executor: ExecutorInterface,
    ) -> None:
        self.user_query_repository = user_query_repository
        self.user_command_repository = user_command_repository
        self.executor = executor

    async def get_user_by_id(self, user_id: ID) -> UserAggregate | None:
        return await self.executor.execute(
            self.user_query_repository.get_by_id, id=user_id
        )

    async def get_user_by_email(self, email: str) -> UserAggregate | None:
        return await self.executor.execute(
            self.user_query_repository.get_by_name, name=email
        )

    async def update_user(self, user_id: ID, user_aggregate: UserAggregate) -> None:
        return await self.executor.execute(
            self.user_command_repository.update,
            id=user_id,
            update_aggregate=user_aggregate,
        )

    async def get_auth_user(self, email: str, password: str) -> UserAggregate | None:
        user = self.get_user_by_email(email)
        if user.validate_password(password):
            return user

    async def delete_user(self, user_id: ID) -> None:
        await self.executor.execute(self.user_command_repository.delete, id=user_id)

    async def create_user(self, new_user: UserAggregate) -> None:
        await self.executor.execute(
            self.user_command_repository.add, aggregate=new_user
        )
