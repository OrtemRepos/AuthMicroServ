from abc import ABC
from functools import singledispatchmethod
from typing import Any

from src.core.domain.entities import User
from src.core.domain.entities.aggregates import UserAggregate
from src.core.domain.service import UserService
from src.core.dto.user import (
    UserBaseIdDTO,
    UserBaseEmailDTO,
    UserUpdateDTO,
    UserFullDTO,
)


class BaseUserUsecase(ABC):
    def __init__(self, user_service: UserService) -> None:
        self.user_service = user_service


class CreateUserUsecase(BaseUserUsecase):
    async def __call__(self, dto: UserFullDTO) -> None:
        user_entity = User(
            id=dto.user_id,
            email=dto.email,
            hashed_password=dto.hashed_password,
            role_ids=dto.role_ids,
        )
        user_aggregate = UserAggregate(user_entity)
        await self.user_service.create_user(user_aggregate)


class DeleteUserUsecase(BaseUserUsecase):
    async def __call__(self, dto: UserBaseIdDTO) -> None:
        await self.user_service.delete_user(dto.user_id)


class UpdateUserUsecase(BaseUserUsecase):
    async def __call__(self, dto: UserUpdateDTO) -> None:
        user_entity = User(
            id=dto.user_id,
            email=dto.email,
            hashed_password=dto.hashed_password,
            role_ids=dto.role_ids,
        )
        updated_aggregate = UserAggregate(user_entity)
        await self.user_service.update_user(updated_aggregate)


class GetUserUsecase(BaseUserUsecase):
    @singledispatchmethod
    async def __call__(
        self, dto: UserBaseEmailDTO | UserBaseIdDTO, dto_output: Any
    ) -> None:
        pass

    @__call__.register
    async def _(self, dto: UserBaseIdDTO, dto_output: Any) -> Any:
        user = await self.user_service.get_user_by_id(dto.user_id)
        user_dto = dto_output.model_validate(user, from_attributes=True)
        return user_dto

    @__call__.register
    async def _(self, dto: UserBaseEmailDTO, dto_output: Any) -> Any:
        user = await self.user_service.get_user_by_email(dto.email)
        user_dto = dto_output.model_validate(user, from_attributes=True)
        return user_dto
