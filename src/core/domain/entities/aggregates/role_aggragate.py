from src.core.domain.entities import Role
from src.core.domain.entities.aggregates import BaseAggregate
from src.core.dto.role import RoleFullDTO


class RoleAggregate(BaseAggregate):
    def __init__(self, role: Role):
        self.role_id = role.id
        self.name = role.name
        self.premission_ids = role.permission_ids

    def role_validate(self, role: RoleFullDTO) -> bool:
        validate_predicate = (
            True
            if self.role_id == role.role_id
            and self.name == role.name
            and self.premission_ids
            else False
        )
        return validate_predicate

    def add_premission(self, premission_id: int):
        self.premission_ids.add(premission_id)

    def remove_premission(self, premission_id: int):
        self.premission_ids.remove(premission_id)

    def validate_premission(self, premission_id: int) -> bool:
        return premission_id in self.premission_ids
