from typing import TypeVar, Union

from .entity import Entity
from .premission import Premission
from .role import Role
from .user import User
from .value_objects import ValueObject
from .aggregates import BaseAggregate

EntityType = TypeVar("EntityType", bound=Entity, covariant=True)
ValueType = TypeVar("ValueType", bound=ValueObject, covariant=True)

DomainEntityType = TypeVar(
    "DomainEntityType", bound=Union[Entity, ValueObject, BaseAggregate]
)

__all__ = [Entity, Premission, Role, User]