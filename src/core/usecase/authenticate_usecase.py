from abc import ABC, abstractclassmethod
from typing import Any

from src.core.domain.service import AuthService
from src.core.dto import AuthTokenDTO, UserAuthDTO, UserRefreshTokenUpdatedDTO


class BaseAuthUsecase(ABC):
    def __init__(self, auth_service: AuthService) -> None:
        self.auth_service = auth_service

    @abstractclassmethod
    async def __call__(self, dto: Any) -> Any:
        pass


class AuthUserWithPassword(BaseAuthUsecase):
    async def __call__(self, dto: UserAuthDTO) -> AuthTokenDTO:
        dto_out = await self.auth_service.auth_user_with_password_and_email(
            dto.email, dto.password.get_secret_value(), dto.aud.aud
        )
        return AuthTokenDTO.model_validate(dto_out)


class AuthUserWithRefreshTokenUsecase(BaseAuthUsecase):
    async def __call__(self, dto: AuthTokenDTO) -> AuthTokenDTO:
        if dto.accsess_token and dto.refresh_token:
            dto_out = await self.auth_service.auth_user_with_refresh_token(
                dto.accsess_token, dto.refresh_token
            )
            return AuthTokenDTO.model_validate(dto_out)
        raise ValueError("Bad credentials")


class AuthUserWithUpdateRoleUsecase(BaseAuthUsecase):
    async def __call__(self, dto: UserRefreshTokenUpdatedDTO) -> AuthTokenDTO:
        dto_out = await self.auth_service.update_token_with_refresh_token(
            dto.user_id, dto.refresh_token, dto.aud.aud
        )
        return AuthTokenDTO.model_validate(dto_out)
