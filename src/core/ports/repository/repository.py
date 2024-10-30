from abc import abstractmethod
from typing import Protocol, TypeVar

from src.core.domain.entities.value_objects import ID
from src.core.domain.entities import DomainEntityType

TOut = TypeVar("TOut", covariant=True, bound=DomainEntityType)
TIn = TypeVar("TIn", contravariant=True, bound=DomainEntityType)


class SyncQueryRepository(Protocol[TOut]):
    @abstractmethod
    def get_by_id(self, entity_id: ID) -> TOut:
        pass

    @abstractmethod
    def get_by_name(self, name: str) -> TOut:
        pass


class AioQueryRepository(Protocol[TOut]):
    @abstractmethod
    async def get_by_id(self, entity_id: ID) -> TOut:
        pass

    @abstractmethod
    async def get_by_name(self, name: str) -> TOut:
        pass


class SyncCommandRepository(Protocol[TIn]):
    @abstractmethod
    def add(self, entity: TIn):
        pass

    @abstractmethod
    def update(self, updated_entity: TIn):
        pass

    @abstractmethod
    def delete(self, entity_id: TIn):
        pass


class AioCommandRepository(Protocol[TIn]):
    @abstractmethod
    async def add(self, entity: TIn):
        pass

    @abstractmethod
    async def update(self, updated_entity: TIn):
        pass

    @abstractmethod
    async def delete(self, entity_id: ID):
        pass
