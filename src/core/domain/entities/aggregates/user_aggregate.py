import bcrypt

from src.core.domain.entities.user import User
from src.core.domain.entities.aggregates import BaseAggregate
from src.core.dto import UserFullDTO


class UserAggregate(BaseAggregate[UserFullDTO, User]):
    def __init__(self, user: User):
        self.user_id = user.id
        self.email = user.email
        self.hashed_password = user.hash_password
        self.role_ids = user.role_ids

    def add_role(self, role_id: int):
        self.role_ids.append(role_id)

    def remove_role(self, role_id: int):
        self.role_ids.remove(role_id)

    def change_password(self, hashed_password: str):
        self.hashed_password = hashed_password

    def change_email(self, email: str):
        self.email = email

    def validate_password(self, password: str) -> bool:
        return bcrypt.checkpw(password.encode(), self.hashed_password.encode())

    def validate_role(self, role_id: int) -> bool:
        return role_id in self.role_ids
