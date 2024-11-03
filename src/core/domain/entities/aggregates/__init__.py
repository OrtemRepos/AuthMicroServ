from typing import TypeVar

from .aggregate import BaseAggregate, Entity
from .role_aggragate import RoleAggregate
from .user_aggregate import UserAggregate

AggregateType = TypeVar("AggregateType", bound=BaseAggregate, covariant=True)
type DomainEntityType = Entity | BaseAggregate


__all__ = ["BaseAggregate", "RoleAggregate", "UserAggregate"]
