from uuid import UUID
from pydantic import EmailStr

from src.core.domain.entities.entity import Entity


class User(Entity[UUID]):
    email: EmailStr
    hash_password: str
    role_ids: set[int]
