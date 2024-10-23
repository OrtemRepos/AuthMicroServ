from typing import TypeVar

from .aggregate import BaseAggregate
from .role_aggragate import RoleAggregate
from .user_aggregate import UserAggregate

AggregateType = TypeVar("AggregateType", bound=BaseAggregate, covariant=True)


__all__ = ["BaseAggregate", "RoleAggregate", "UserAggregate"]
