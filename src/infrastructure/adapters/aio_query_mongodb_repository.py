from pymongo import AsyncMongoClient

from src.core.domain.entities import Premission, Role, User
from src.core.domain.entities.aggregates import RoleAggregate, UserAggregate
from src.core.domain.entities.value_objects import ID
from src.core.ports.repository import AioQueryRepository


class QueryMongoRepositoryUser(AioQueryRepository[UserAggregate]):
    def __init__(self, client: AsyncMongoClient) -> None:
        self._client = client
        self._collection = self._client["auth"]["user"]

    async def get_by_id(self, entity_id: ID) -> UserAggregate:
        entity = await self._collection.find_one({"id": entity_id})
        if entity:
            entity_model = User.model_validate(**entity)
            return UserAggregate(entity_model)
        else:
            raise ValueError(f"Not fount entity with id {entity_id}")

    async def get_by_name(self, email: str) -> UserAggregate:
        entity = await self._collection.find_one({"name": email})
        if entity:
            entity_model = User.model_validate(**entity)
            return UserAggregate(entity_model)
        else:
            raise ValueError(f"Not fount entity with {email=}")


class QueryMongoRepositoryRole(AioQueryRepository[RoleAggregate]):
    def __init__(self, client: AsyncMongoClient) -> None:
        self._client = client
        self._collection = self._client["auth"]["role"]

    async def get_by_id(self, entity_id: ID) -> RoleAggregate:
        entity = await self._collection.find_one({"id": entity_id})
        if entity:
            entity_model = Role.model_validate(**entity)
            return RoleAggregate(entity_model)
        else:
            raise ValueError(f"Not fount entity with id {entity_id}")

    async def get_by_name(self, name: str) -> RoleAggregate:
        entity = await self._collection.find_one({"name": name})
        if entity:
            entity_model = Role.model_validate(**entity)
            return RoleAggregate(entity_model)
        else:
            raise ValueError(f"Not fount entity with {name=}")


class QueryMongoRepositoryPremission(AioQueryRepository[Premission]):
    def __init__(self, client: AsyncMongoClient) -> None:
        self._client = client
        self._collection = self._client["auth"]["premission"]

    async def get_by_id(self, entity_id: ID) -> Premission:
        entity = await self._collection.find_one({"id": entity_id})
        if entity:
            return Premission(**entity)
        else:
            raise ValueError(f"Not fount entity with id {entity_id}")

    async def get_by_name(self, name: str) -> Premission:
        entity = await self._collection.find_one({"name": name})
        if entity:
            return Premission(**entity)
        else:
            raise ValueError(f"Not fount entity with name {name}")
