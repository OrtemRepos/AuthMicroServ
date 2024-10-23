from abc import ABC
from functools import singledispatchmethod
from typing import Any, Protocol

from src.core.domain.entities import Premission
from src.core.domain.service import PremissionService
from src.core.dto.premission import (
    PremissionFullDTO,
    PremissionBaseIdDTO,
    PremissionBaseNameDTO,
    PremissionUpdateDTO,
)


class BasePremissionUsecaseInterface(Protocol):
    def __init__(self, premission_service: PremissionService) -> None:
        pass


class BasePremissionUsecase(ABC, BasePremissionUsecaseInterface):
    def __init__(self, premission_service: PremissionService) -> None:
        self.premission_service = premission_service


class CreatePremissionUsecase(BasePremissionUsecase):
    async def __call__(self, premission: PremissionFullDTO) -> None:
        premission_entity = Premission(
            id=premission.premission_id, name=premission.name
        )
        await self.premission_service.create_premission(premission_entity)


class DeletePremissionUsecase(BasePremissionUsecase):
    async def __call__(self, premission: PremissionBaseIdDTO) -> None:
        await self.premission_service.delete_premisson(premission.premission_id)


class UpdatePremissionUsecase(BasePremissionUsecase):
    async def __call__(
        self, premission_id: PremissionBaseIdDTO, premission: PremissionUpdateDTO
    ) -> None:
        premission_entity = Premission(
            id=premission_id.premission_id,
            name=premission.name,
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
        premission = await self.premission_service.get_premission_by_id(
            premission_id.premission_id
        )
        premission_dto = dto.model_validate(premission, from_attributes=True)
        return premission_dto

    @__call__.register
    async def _(self, premission_id: PremissionBaseNameDTO, dto: Any) -> Any:
        premission = await self.premission_service.get_premission_by_name(
            premission_id.name
        )
        premission_dto = dto.model_validate(premission, from_attributes=True)
        return premission_dto
