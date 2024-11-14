from src.core.domain.entities import Premission
from src.core.domain.service import PremissionService
from src.core.dto.premission import PremissionDTO


class BasePremissionUsecase:
    def __init__(self, premission_service: PremissionService) -> None:
        self.premission_service = premission_service


class CreatePremissionUsecase(BasePremissionUsecase):
    async def __call__(self, dto: PremissionDTO) -> None:
        premission_entity = Premission(id=dto.premission_id, name=dto.name)  # type: ignore
        await self.premission_service.create_premission(premission_entity)


class DeletePremissionUsecase(BasePremissionUsecase):
    async def __call__(self, dto: PremissionDTO) -> None:
        await self.premission_service.delete_premisson(dto.premission_id)


class UpdatePremissionUsecase(BasePremissionUsecase):
    async def __call__(self, dto: PremissionDTO) -> None:
        premission_entity = Premission(
            id=dto.premission_id,  # type: ignore
            name=dto.name,  # type: ignore
        )
        await self.premission_service.update_premission(premission_entity)


class GetPremissionUsecase(BasePremissionUsecase):
    async def __call__(self, dto: PremissionDTO) -> PremissionDTO:
        if dto.premission_id is not None:
            result = await self.premission_service.get_premission_by_id(
                dto.premission_id
            )
            return PremissionDTO(premission_id=result.id, name=result.name)
        elif dto.name is not None:
            result = await self.premission_service.get_premission_by_name(
                dto.name
            )
            return PremissionDTO(premission_id=result.id, name=result.name)
        else:
            raise TypeError(
                f'Argument "dto" have incompatible type "{type(dto)}"'
            )
