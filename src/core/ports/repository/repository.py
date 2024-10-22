from abc import abstractmethod
from typing import Protocol

from src.core.domain.entities import DomainEntityType
from src.core.domain.entities.value_objects import ID


class SyncQueryRepository(Protocol[DomainEntityType]):
    @abstractmethod
    def get_by_id(entity_id: ID) -> DomainEntityType:
        pass

    @abstractmethod
    def get_by_name(name: str) -> DomainEntityType:
        pass


class AioQueryRepository(Protocol[DomainEntityType]):
    @abstractmethod
    async def get_by_id(entity_id: ID) -> DomainEntityType:
        pass

    @abstractmethod
    async def get_by_name(name: str) -> DomainEntityType:
        pass


class SyncCommandRepository(Protocol[DomainEntityType]):
    @abstractmethod
    def add(entity: DomainEntityType):
        pass

    @abstractmethod
    def update(updated_entity: DomainEntityType):
        pass

    @abstractmethod
    def delete(entity: DomainEntityType):
        pass


class AioCommandRepository(Protocol[DomainEntityType]):
    @abstractmethod
    async def add(entity: DomainEntityType):
        pass

    @abstractmethod
    async def update(updated_entity: DomainEntityType):
        pass

    @abstractmethod
    async def delete(entity: DomainEntityType):
        pass
