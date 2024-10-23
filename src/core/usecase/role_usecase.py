from abc import ABC
from functools import singledispatchmethod
from typing import Any, Protocol

from src.core.domain.entities.aggregates import RoleAggregate
from src.core.domain.entities import Role
from src.core.domain.service import RoleService
from src.core.dto import (
    RoleFullDTO,
    RoleBaseIdDTO,
    RoleBaseNameDTO,
    RoleUpdateDTO,
)


class BaseRoleUsecaseInterface(Protocol):
    def __init__(self, role_service: RoleService) -> None:
        pass


class BaseRoleUsecase(BaseRoleUsecaseInterface, ABC):
    def __init__(self, role_service: RoleService) -> None:
        self.role_service = role_service


class CreateRoleUsecase(BaseRoleUsecase):
    async def __call__(self, role: RoleFullDTO) -> None:
        role_entity = Role(
            id=role.role_id, name=role.name, permission_ids=role.premission_ids
        )
        role_aggregate = RoleAggregate(role_entity)
        await self.role_service.create_role(role_aggregate)


class DeleteRoleUsecase(BaseRoleUsecase):
    async def __call__(self, role: RoleBaseIdDTO) -> None:
        await self.role_service.delete_role(role.role_id)


class UpdateRoleUsecase(BaseRoleUsecase):
    async def __call__(self, role_id: RoleBaseIdDTO, role: RoleUpdateDTO) -> None:
        role_entity = Role(
            id=role_id.role_id, name=role.name, permission_ids=role.premission_ids
        )
        updated_aggregate = RoleAggregate(role_entity)
        await self.role_service.update_role(updated_aggregate)


class GetRoleUsecase(BaseRoleUsecase):
    @singledispatchmethod
    async def __call__(
        self, role_id: RoleBaseIdDTO | RoleBaseNameDTO, dto: Any
    ) -> None:
        pass

    @__call__.register
    async def _(self, role_id: RoleBaseIdDTO, dto: Any) -> Any:
        role = await self.role_service.get_role_by_id(role_id.role_id)
        role_dto = dto.model_validate(role, from_attributes=True)
        return role_dto

    @__call__.register
    async def _(self, role_id: RoleBaseNameDTO, dto: Any) -> Any:
        role = await self.role_service.get_role_by_name(role_id.name)
        role_dto = dto.model_validate(role, from_attributes=True)
        return role_dto
