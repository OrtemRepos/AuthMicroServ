from src.core.domain.entities.aggregates import UserAggregate
from src.core.domain.service import UserService
from src.core.dto.user import UserDTO


class BaseUserUsecase:
    def __init__(self, user_service: UserService) -> None:
        self.user_service = user_service


class CreateUserUsecase(BaseUserUsecase):
    async def __call__(self, dto: UserDTO) -> None:
        user_aggregate = UserAggregate.from_dto(dto)
        await self.user_service.create_user(user_aggregate)


class DeleteUserUsecase(BaseUserUsecase):
    async def __call__(self, dto: UserDTO) -> None:
        if dto.user_id is not None:
            await self.user_service.delete_user(dto.user_id)


class UpdateUserUsecase(BaseUserUsecase):
    async def __call__(self, dto: UserDTO) -> None:
        user_aggregate = UserAggregate.from_dto(dto)
        await self.user_service.update_user(user_aggregate)


class GetUserUsecase(BaseUserUsecase):
    async def __call__(self, dto: UserDTO) -> UserDTO:
        if dto.user_id is not None:
            aggregate = await self.user_service.get_user_by_id(dto.user_id)
            return aggregate.to_dto()
        elif dto.email is not None:
            aggregate = await self.user_service.get_user_by_email(dto.email)
            return aggregate.to_dto()
        else:
            raise TypeError(
                f'Argument "dto" have incompatible type "{type(dto)}"'
                f'Expected "{self.__annotations__["dto"]}"'
            )
