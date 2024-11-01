import redis.asyncio as redis

from src.config import RedisSettings
from src.core.domain.entities import RefreshToken
from src.core.domain.entities.value_objects import ID
from src.core.ports.repository import AioCommandRepository


class CommandRedisRepository(AioCommandRepository[RefreshToken]):
    def __init__(self, client: redis.Redis, config: RedisSettings = RedisSettings()):
        self._client: redis.Redis = client
        self.config = config

    async def add(self, entity: RefreshToken):
        self._client.set(
            str(entity.id), entity.token, ex=self.config.refresh_token_expire_ms
        )

    async def update(self, updated_entity: RefreshToken):
        self._client.set(
            str(updated_entity.id),
            updated_entity.token,
            ex=self.config.refresh_token_expire_ms,
        )

    async def delete(self, entity_id: ID):
        self._client.delete(str(entity_id))
