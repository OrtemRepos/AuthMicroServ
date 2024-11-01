from pymongo import AsyncMongoClient

from src.core.domain.entities.value_objects import ID
from src.core.ports.repository import AioCommandRepository, TIn


class CommandMongoRepository(AioCommandRepository[TIn]):
    def __init__(
        self, client: AsyncMongoClient, db_name: str, collection_name: str
    ) -> None:
        self._client = client
        self._db = client[db_name]
        self._collection = self._db[collection_name]

    async def add(self, entity: TIn) -> None:
        dict_model = entity.model_dump()
        await self._collection.insert_one(dict_model)

    async def update(self, updated_entity: TIn):
        dict_model = updated_entity.model_dump()
        await self._collection.update_one({"id": dict_model["id"]}, dict_model)

    async def delete(self, entity_id: ID):
        await self._collection.delete_one({"id": entity_id})
