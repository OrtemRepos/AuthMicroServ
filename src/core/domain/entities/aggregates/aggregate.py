from typing import Any, Protocol, TypeVar
from abc import ABC, abstractmethod

from pydantic import BaseModel


EntityType = TypeVar("EntityType", bound=BaseModel, contravariant=True)


class Aggregate(Protocol):
    @classmethod
    @abstractmethod
    def from_dto(cls: "Aggregate", dto: Any) -> "Aggregate":
        pass

    @classmethod
    @abstractmethod
    def from_entity(cls: "Aggregate", entity: EntityType) -> "Aggregate":
        pass

    @abstractmethod
    def to_dto(self, dto_type: Any) -> Any:
        pass


class BaseAggregate(ABC):
    @classmethod
    def from_dto(cls, dto: Any) -> "BaseAggregate":
        return cls(**dto)

    @classmethod
    def from_entity(cls, entity: EntityType) -> "BaseAggregate":
        return cls(**entity.__dict__)

    def to_dto(self, dto_type: Any) -> Any:
        return dto_type.model_validate(self, from_attributes=True)
