from typing import TypeVar

from .entity import Entity
from .premission import Premission
from .role import Role
from .user import User
from .value_objects import ValueObject
from .aggregates import BaseAggregate
from .token import RefreshToken

EntityType = TypeVar("EntityType", bound=Entity, covariant=True)
ValueType = TypeVar("ValueType", bound=ValueObject, covariant=True)
AggregateType = TypeVar("AggregateType", bound=BaseAggregate, covariant=True)

type DomainEntityType = ValueObject | Entity | BaseAggregate

__all__ = ["Entity", "Premission", "Role", "User", "RefreshToken"]
