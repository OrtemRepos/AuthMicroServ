from src.core.domain.entities.role import Role
from src.core.domain.entities.aggregates import BaseAggregate
from src.core.dto import RoleFullDTO


class RoleAggregate(BaseAggregate[RoleFullDTO]):
    def __init__(self, role: Role):
        self.role_id = role.id
        self.name = role.name
        self.premission_ids = role.permission_ids

    def role_validate(self, role: RoleFullDTO) -> bool:
        validate_predicate = (
            self.role_id == role.role_id
            and self.name == role.name
            and self.premission_ids
        )
        return validate_predicate

    def add_premission(self, premission_id: int):
        self.premission_ids.append(premission_id)

    def remove_premission(self, premission_id: int):
        self.premission_ids.remove(premission_id)

    def validate_premission(self, premission_id: int) -> bool:
        return premission_id in self.premission_ids
