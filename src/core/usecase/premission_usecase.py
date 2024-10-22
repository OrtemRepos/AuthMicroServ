from abc import ABC
from functools import singledispatchmethod

from src.core.domain.entities.aggregates import PremissionAggregate
from src.core.domain.entities import Premission
from src.core.domain.service import PremissionService
from src.core.dto import (
    PremissionFullDTO,
    PremissionBaseIdDTO,
    PremissionBaseNameDTO,
    PremissionUpdateDTO,
    PremissionBaseDTO,
)


class BasePremissionUsecase(ABC):
    def __init__(self, premission_service: PremissionService) -> None:
        self.premission_service = premission_service


class CreatePremissionUsecase(BasePremissionUsecase):
    async def __call__(self, premission: PremissionFullDTO) -> None:
        premission_entity = Premission(
            id=premission.premission_id, permission_ids=premission.premission_ids
        )
        premission_aggregate = PremissionAggregate(premission_entity)
        await self.Premission_service.create_Premission(premission_aggregate)


class DeletePremissionUsecase(BasePremissionUsecase):
    async def __call__(self, premission: PremissionBaseIdDTO) -> None:
        await self.premission_service.delete_Premission(premission.premission_id)


class UpdatePremissionUsecase(BasePremissionUsecase):
    async def __call__(
        self, Premission_id: PremissionBaseIdDTO, premission: PremissionUpdateDTO
    ) -> None:
        premission_entity = premission(
            id=Premission_id.premission_id,
            name=premission.name,
            premission_ids=premission.premission_ids,
        )
        updated_aggregate = PremissionAggregate(premission_entity)
        await self.premission_service.update_Premission(updated_aggregate)


class GetPremissionUsecase(BasePremissionUsecase):
    @singledispatchmethod
    async def __call__(
        self,
        premission_id: PremissionBaseIdDTO | PremissionBaseNameDTO,
        dto: PremissionBaseDTO,
    ) -> PremissionBaseDTO:
        pass

    @__call__.register
    async def _(
        self, premission_id: PremissionBaseIdDTO, dto: PremissionBaseDTO
    ) -> PremissionBaseDTO:
        premission = await self.premission_service.get_premission_by_id(
            premission_id.premission_id
        )
        premission_dto = dto.model_validate(premission, from_attributes=True)
        return premission_dto

    @__call__.register
    async def _(
        self, premission_id: PremissionBaseNameDTO, dto: PremissionBaseDTO
    ) -> PremissionBaseDTO:
        premission = await self.premission_service.get_premission_by_name(
            premission_id.premission_id
        )
        premission_dto = dto.model_validate(premission, from_attributes=True)
        return premission_dto
