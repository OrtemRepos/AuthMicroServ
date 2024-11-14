import bcrypt

from src.core.domain.entities.aggregates import BaseAggregate
from src.core.domain.entities.user import User
from src.core.dto.user import UserDTO


class UserAggregate(BaseAggregate[User]):
    def __init__(self, user: User):
        self.user_id = user.id
        self.email = user.email
        self.hashed_password = user.hashed_password
        self.role_ids = user.role_ids
        self.entity = user

    def add_role(self, role_id: int):
        self.role_ids.add(role_id)

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

    @classmethod
    def model_validate(cls, data: dict) -> "UserAggregate":
        entity = User(**data)
        return cls(entity)

    @classmethod
    def from_dto(cls, dto: UserDTO) -> "UserAggregate":
        entity = User(
            id=dto.user_id,  # type: ignore
            email=dto.email,  # type: ignore
            hashed_password=dto.hashed_password,  # type: ignore
            role_ids=dto.role_ids,  # type: ignore
        )
        return cls(entity)

    def to_dto(self) -> UserDTO:
        return UserDTO.model_validate(self, from_attributes=True)
