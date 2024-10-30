from src.core.domain.entities.value_objects import ID
from src.core.domain.entities.aggregates.user_aggregate import UserAggregate
from src.core.ports.repository import QueryRepositoryType, CommandRepositoryType
from src.infrastructure.executor import ExecutorInterface


class UserService:
    def __init__(
        self,
        user_query_repository: QueryRepositoryType[UserAggregate],
        user_command_repository: CommandRepositoryType[UserAggregate],
        executor: ExecutorInterface[UserAggregate],
    ) -> None:
        self.user_query_repository = user_query_repository
        self.user_command_repository = user_command_repository
        self.executor = executor

    async def get_user_by_id(self, user_id: ID) -> UserAggregate:
        result = await self.executor.execute(
            self.user_query_repository.get_by_id, user_id
        )
        if result:
            return result
        raise ValueError(f"User with {user_id=} not found")

    async def get_user_by_email(self, email: str) -> UserAggregate:
        user = await self.executor.execute(
            self.user_query_repository.get_by_name, email
        )
        if user:
            return user
        raise ValueError(f"User with {email=} not found")

    async def update_user(self, user_aggregate: UserAggregate) -> None:
        await self.executor.execute(
            self.user_command_repository.update,
            user_aggregate,
        )

    async def get_auth_user(self, email: str, password: str) -> UserAggregate:
        user = await self.get_user_by_email(email)
        if user.validate_password(password):
            return user
        raise ValueError("User credentials are not valid")

    async def delete_user(self, user_id: ID) -> None:
        await self.executor.execute(self.user_command_repository.delete, user_id)

    async def create_user(self, new_user: UserAggregate) -> None:
        await self.executor.execute(self.user_command_repository.add, new_user)
