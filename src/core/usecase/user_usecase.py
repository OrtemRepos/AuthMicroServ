from abc import ABC
from functools import singledispatchmethod

from src.core.domain.entities import User
from src.core.domain.entities.aggregates import UserAggregate
from src.core.domain.service import UserService
from src.core.dto import (
    UserFullDTO,
    UserBaseIdDTO,
    UserBaseEmailDTO,
    UserUpdateDTO,
    UserBaseDTO,
)


class BaseUserUsecase(ABC):
    def __init__(self, user_service: UserService) -> None:
        self.user_service = user_service


class CreateUserUsecase(BaseUserUsecase):
    async def __call__(self, user: UserFullDTO) -> None:
        user_entity = User(
            id=user.user_id,
            email=user.email,
            hashed_password=user.hashed_password,
            role_ids=user.role_ids,
        )
        user_aggregate = UserAggregate(user_entity)
        await self.user_service.create_user(user_aggregate)


class DeleteUserUsecase(BaseUserUsecase):
    async def __call__(self, user: UserBaseIdDTO) -> None:
        await self.user_service.delete_user(user.user_id)


class UpdateUserUsecase(BaseUserUsecase):
    async def __call__(self, user_id: UserBaseIdDTO, user: UserUpdateDTO) -> None:
        user_entity = User(
            id=user_id.user_id,
            email=user.email,
            hashed_password=user.hashed_password,
            role_ids=user.role_ids,
        )
        updated_aggregate = UserAggregate(user_entity)
        await self.user_service.update_user(user.user_id, updated_aggregate)


class GetUserUsecase(BaseUserUsecase):
    @singledispatchmethod
    async def __call__(
        self, user_id: UserBaseEmailDTO | UserBaseIdDTO, dto: UserBaseDTO
    ) -> UserBaseDTO:
        pass

    @__call__.register
    async def _(self, user_id: UserBaseIdDTO, dto: UserBaseDTO) -> UserBaseDTO:
        user = await self.user_service.get_user_by_id(user_id)
        user_dto = dto.model_validate(user, from_attributes=True)
        return user_dto

    @__call__.register
    async def _(self, user_id: UserBaseEmailDTO, dto: UserBaseDTO) -> UserBaseDTO:
        user = await self.user_service.get_user_by_email(user_id)
        user_dto = dto.model_validate(user, from_attributes=True)
        return user_dto
