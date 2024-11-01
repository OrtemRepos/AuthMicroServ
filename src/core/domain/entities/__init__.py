from .aggregates import BaseAggregate
from .entity import Entity
from .premission import Premission
from .role import Role
from .token_entity import RefreshToken
from .user import User
from .value_objects import AccsesToken

type DomainEntityType = Entity | BaseAggregate

__all__ = ["Entity", "Premission", "Role", "User", "RefreshToken", "AccsesToken"]
