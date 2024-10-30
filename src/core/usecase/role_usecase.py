from abc import ABC
from functools import singledispatchmethod
from typing import Any

from src.core.domain.entities.aggregates import RoleAggregate
from src.core.domain.entities import Role
from src.core.domain.service import RoleService
from src.core.dto import (
    RoleFullDTO,
    RoleBaseIdDTO,
    RoleBaseNameDTO,
    RoleUpdateDTO,
)


class BaseRoleUsecase(ABC):
    def __init__(self, role_service: RoleService) -> None:
        self.role_service = role_service


class CreateRoleUsecase(BaseRoleUsecase):
    async def __call__(self, dto: RoleFullDTO) -> None:
        role_entity = Role(
            id=dto.role_id, name=dto.name, permission_ids=dto.premission_ids
        )
        role_aggregate = RoleAggregate(role_entity)
        await self.role_service.create_role(role_aggregate)


class DeleteRoleUsecase(BaseRoleUsecase):
    async def __call__(self, dto: RoleBaseIdDTO) -> None:
        await self.role_service.delete_role(dto.role_id)


class UpdateRoleUsecase(BaseRoleUsecase):
    async def __call__(self, dto: RoleUpdateDTO) -> None:
        role_entity = Role(
            id=dto.role_id, name=dto.name, permission_ids=dto.premission_ids
        )
        updated_aggregate = RoleAggregate(role_entity)
        await self.role_service.update_role(updated_aggregate)


class GetRoleUsecase(BaseRoleUsecase):
    @singledispatchmethod
    async def __call__(
        self, dto: RoleBaseIdDTO | RoleBaseNameDTO, dto_out: Any
    ) -> None:
        pass

    @__call__.register
    async def _(self, dto: RoleBaseIdDTO, dto_out: Any) -> Any:
        dto_out = await self.role_service.get_role_by_id(dto.role_id)
        role_dto = dto_out.model_validate(dto_out, from_attributes=True)
        return role_dto

    @__call__.register
    async def _(self, dto: RoleBaseNameDTO, dto_out: Any) -> Any:
        dto_out = await self.role_service.get_role_by_name(dto.name)
        role_dto = dto_out.model_validate(dto_out, from_attributes=True)
        return role_dto
