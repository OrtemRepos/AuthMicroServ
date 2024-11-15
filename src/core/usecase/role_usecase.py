from src.core.domain.entities.aggregates import RoleAggregate
from src.core.domain.service import RoleService
from src.core.dto import RoleDTO


class BaseRoleUsecase:
    def __init__(self, role_service: RoleService) -> None:
        self.role_service = role_service


class CreateRoleUsecase(BaseRoleUsecase):
    async def __call__(self, dto: RoleDTO) -> None:
        role_aggregate = RoleAggregate.from_dto(dto)
        await self.role_service.create_role(role_aggregate)


class DeleteRoleUsecase(BaseRoleUsecase):
    async def __call__(self, dto: RoleDTO) -> None:
        if dto.role_id is not None:
            await self.role_service.delete_role(dto.role_id)
        raise TypeError("Not valid dto")


class UpdateRoleUsecase(BaseRoleUsecase):
    async def __call__(self, dto: RoleDTO) -> None:
        updated_aggregate = RoleAggregate.from_dto(dto)
        await self.role_service.update_role(updated_aggregate)


class GetRoleUsecase(BaseRoleUsecase):
    async def __call__(self, dto: RoleDTO) -> RoleDTO:
        if dto.role_id is not None:
            aggregate = await self.role_service.get_role_by_id(dto.role_id)
            return aggregate.to_dto()
        elif dto.name is not None:
            aggregate = await self.role_service.get_role_by_name(dto.name)
            return aggregate.to_dto()
        else:
            raise TypeError(
                f'Argument "dto" have incompatible type "{type(dto)}"'
                f'Expected "{self.__annotations__["dto"]}"'
            )
