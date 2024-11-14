from src.core.domain.entities import Role
from src.core.domain.entities.aggregates import BaseAggregate
from src.core.dto.role import RoleDTO


class RoleAggregate(BaseAggregate[Role]):
    def __init__(self, role: Role):
        self.role_id = role.id
        self.name = role.name
        self.premission_ids = role.permission_ids
        self.entity = role

    def role_validate(self, role: RoleDTO) -> bool:
        validate_predicate = bool(
            self.role_id == role.role_id
            and self.name == role.name
            and self.premission_ids
        )
        return validate_predicate

    def add_premission(self, premission_id: int):
        self.premission_ids.add(premission_id)

    def remove_premission(self, premission_id: int):
        self.premission_ids.remove(premission_id)

    def validate_premission(self, premission_id: int) -> bool:
        return premission_id in self.premission_ids

    @classmethod
    def model_validate(cls, data: dict) -> "RoleAggregate":
        entity = Role(**data)
        return cls(entity)

    @classmethod
    def from_dto(cls, dto: RoleDTO) -> "RoleAggregate":
        entity = Role(
            id=dto.role_id,  # type: ignore
            name=dto.name,  # type: ignore
            permission_ids=dto.premission_ids,  # type: ignore
        )
        return cls(entity)

    def to_dto(self) -> RoleDTO:
        return RoleDTO(
            role_id=self.role_id,
            name=self.name,
            premission_ids=self.premission_ids,
        )
