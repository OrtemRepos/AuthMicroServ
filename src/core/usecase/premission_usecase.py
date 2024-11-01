from abc import ABC
from functools import singledispatchmethod
from typing import Any

from src.core.domain.entities import Premission
from src.core.domain.service import PremissionService
from src.core.dto.premission import (
    PremissionBaseIdDTO,
    PremissionBaseNameDTO,
    PremissionFullDTO,
    PremissionUpdateDTO,
)


class BasePremissionUsecase(ABC):
    def __init__(self, premission_service: PremissionService) -> None:
        self.premission_service = premission_service


class CreatePremissionUsecase(BasePremissionUsecase):
    async def __call__(self, dto: PremissionFullDTO) -> None:
        premission_entity = Premission(id=dto.premission_id, name=dto.name)
        await self.premission_service.create_premission(premission_entity)


class DeletePremissionUsecase(BasePremissionUsecase):
    async def __call__(self, dto: PremissionBaseIdDTO) -> None:
        await self.premission_service.delete_premisson(dto.premission_id)


class UpdatePremissionUsecase(BasePremissionUsecase):
    async def __call__(
        self, premission_id: PremissionBaseIdDTO, dto: PremissionUpdateDTO
    ) -> None:
        premission_entity = Premission(
            id=premission_id.premission_id,
            name=dto.name,
        )
        await self.premission_service.update_premission(premission_entity)


class GetPremissionUsecase(BasePremissionUsecase):
    @singledispatchmethod
    async def __call__(
        self,
        premission_id: PremissionBaseIdDTO | PremissionBaseNameDTO,
        dto: Any,
    ) -> None:
        pass

    @__call__.register
    async def _(self, premission_id: PremissionBaseIdDTO, dto: Any) -> Any:
        dto = await self.premission_service.get_premission_by_id(
            premission_id.premission_id
        )
        premission_dto = dto.model_validate(dto, from_attributes=True)
        return premission_dto

    @__call__.register
    async def _(self, premission_id: PremissionBaseNameDTO, dto: Any) -> Any:
        dto = await self.premission_service.get_premission_by_name(premission_id.name)
        premission_dto = dto.model_validate(dto, from_attributes=True)
        return premission_dto
