from core.domain.entities.value_objects import (
    ID,
    AccsesToken,
    RefreshToken,
    TokenPayload,
)
from src.infrastructure.token_provider import TokenProviderInterface
from src.core.ports.repository.repository import QueryRepositoryT, CommandRepositoryT
from src.infrastructure.executor import ExecutorInterface


class TokenService:
    def __init__(
        self,
        token_provider: TokenProviderInterface,
        token_repository_query: QueryRepositoryT,
        token_repository_command: CommandRepositoryT,
        executor: ExecutorInterface,
    ) -> None:
        self.token_provider = token_provider
        self.token_repository_query = token_repository_query
        self.token_repository_command = token_repository_command
        self.executor = executor

    async def get_refresh_token_by_id(self, user_id: ID) -> RefreshToken:
        return await self.executor.execute(
            self.token_repository_query.get_by_id(entity_id=user_id)
        )

    async def get_refresh_token_by_token(self, token: RefreshToken) -> RefreshToken:
        return await self.executor.execute(
            self.token_repository_query.get_by_name(name=token)
        )

    async def set_refresh_token(self, user_id: ID) -> RefreshToken:
        refresh_token: RefreshToken = self.token_provider.generate_refresh_token()
        await self.executor.execute(
            self.token_repository_command.update(user_id, refresh_token)
        )
        return refresh_token

    async def create_refresh_token(self, user_id: ID) -> RefreshToken:
        refresh_token: RefreshToken = self.token_provider.generate_refresh_token()
        await self.executor.execute(
            self.token_repository_command.add, user_id, refresh_token
        )

    def decode_accses_token(self, token: AccsesToken) -> TokenPayload:
        return self.token_provider.decode(token)

    def create_accses_token(
        self, user_id: ID, aud: str, role_ids: list[int]
    ) -> AccsesToken:
        return self.token_provider.generate_token(
            user_id=user_id, aud=aud, role_ids=role_ids
        )

    async def refresh_accses_token(
        self, accses_token: AccsesToken
    ) -> tuple[AccsesToken, RefreshToken]:
        payload = self.decode_accses_token(accses_token)
        new_accses_token = self.create_accses_token(
            user_id=payload.sub, aud=payload.aud, role_ids=payload.roles
        )
        new_refresh_token = self.create_refresh_token(user_id=payload.sub)
        return new_accses_token, new_refresh_token

    async def delete_refresh_token(self, user_id: ID):
        return self.token_repository_command.delete(entity_id=user_id)