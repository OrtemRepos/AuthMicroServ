from pydantic import EmailStr

from src.core.domain.entities.entity import Entity


class User(Entity):
    email: EmailStr
    hashed_password: str
    role_ids: set[int]
