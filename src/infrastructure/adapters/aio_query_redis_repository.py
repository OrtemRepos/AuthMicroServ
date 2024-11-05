import redis.asyncio as redis

from src.config import RedisSettings
from src.core.domain.entities import RefreshToken
from src.core.domain.entities.value_objects import ID
from src.core.ports.repository import AioQueryRepository


class QueryRedisRepository(AioQueryRepository[RefreshToken]):
    def __init__(self, client: redis.Redis, config: RedisSettings):
        self.config = config
        self._client = client

    async def get_by_id(self, entity_id: ID) -> RefreshToken:
        result = await self._client.get(str(entity_id))
        entity = RefreshToken(id=entity_id, token=result)
        return entity

    async def get_by_name(self, name: str) -> RefreshToken:
        raise NotImplementedError("Not supporting for Redis.")
