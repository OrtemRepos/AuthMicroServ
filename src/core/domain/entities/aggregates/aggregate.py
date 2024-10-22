from typing import Protocol
from abc import ABC, abstractmethod

from src.core.domain.entities import EntityType
from src.core.dto import FullDTO, DTOType


class Aggregate(Protocol[FullDTO, EntityType]):
    @classmethod
    @abstractmethod
    def from_dto(cls: "Aggregate", dto: FullDTO) -> "Aggregate":
        pass

    @classmethod
    @abstractmethod
    def from_entity(cls: "Aggregate", entity: EntityType) -> "Aggregate":
        return cls(**entity.model_dump())

    @abstractmethod
    def to_dto(self, dto_type: DTOType) -> DTOType:
        pass


class BaseAggregate(Protocol[FullDTO, EntityType], ABC):
    @classmethod
    def from_dto(cls, dto: FullDTO) -> "BaseAggregate":
        return cls(**dto)

    @classmethod
    def from_entity(cls, entity: EntityType) -> "BaseAggregate":
        cls(**entity.__dict__)

    def to_dto(self, dto_type: DTOType) -> DTOType:
        return dto_type.model_validate(self, from_attributes=True)
