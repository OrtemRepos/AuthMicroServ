from abc import abstractmethod
from typing import Protocol

from src.core.domain.entities import DomainEntityType
from src.core.domain.entities.value_objects import ID


class SyncQueryRepository(Protocol):
    @abstractmethod
    def get_by_id(self, entity_id: ID) -> DomainEntityType:
        pass

    @abstractmethod
    def get_by_name(self, name: str) -> DomainEntityType:
        pass


class AioQueryRepository(Protocol):
    @abstractmethod
    async def get_by_id(self, entity_id: ID) -> DomainEntityType:
        pass

    @abstractmethod
    async def get_by_name(self, name: str) -> DomainEntityType:
        pass


class SyncCommandRepository(Protocol):
    @abstractmethod
    def add(self, entity: DomainEntityType):
        pass

    @abstractmethod
    def update(self, updated_entity: DomainEntityType):
        pass

    @abstractmethod
    def delete(self, entity_id: ID):
        pass


class AioCommandRepository(Protocol):
    @abstractmethod
    async def add(self, entity: DomainEntityType):
        pass

    @abstractmethod
    async def update(self, updated_entity: DomainEntityType):
        pass

    @abstractmethod
    async def delete(self, entity_id: ID):
        pass
