from abc import ABC, abstractmethod
from typing import Any, Protocol, TypeVar

from src.core.domain.entities.entity import Entity

EntityType = TypeVar("EntityType", bound=Entity, covariant=True)


class Aggregate(Protocol[EntityType]):
    @classmethod
    @abstractmethod
    def from_dto(cls: "Aggregate", dto: Any) -> "Aggregate":
        pass

    @abstractmethod
    def to_dto(self) -> Any:
        pass

    @abstractmethod
    def to_entity(self) -> EntityType:
        pass


class BaseAggregate(Aggregate[EntityType], ABC):
    entity: EntityType

    def __init__(self, *args, **kwargs):
        pass

    @abstractmethod
    @classmethod
    def from_dto(cls, dto: Any) -> "BaseAggregate":
        pass

    @abstractmethod
    def to_dto(self) -> Any:
        pass

    def to_entity(self) -> EntityType:
        return self.entity

    def model_dump(self) -> dict:
        return self.entity.model_dump()

    @classmethod
    @abstractmethod
    def model_validate(cls, data: dict) -> "BaseAggregate":
        pass
