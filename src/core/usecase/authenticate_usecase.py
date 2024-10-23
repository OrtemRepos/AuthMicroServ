from abc import ABC
from typing import Protocol
from src.core.domain.service import AuthService
from src.core.dto import AuthTokenDTO, UserAuthDTO, UserRefreshTokenUpdatedDTO


class BaseAuthUsecaseInterface(Protocol):
    def __init__(self, auth_service: AuthService) -> None:
        pass


class BaseAuthUsecase(ABC, BaseAuthUsecaseInterface):
    def __init__(self, auth_service: AuthService) -> None:
        self.auth_service = auth_service


class AuthUserWithPassword(BaseAuthUsecase):
    async def __call__(self, auth: UserAuthDTO) -> AuthTokenDTO:
        dto = await self.auth_service.auth_user_with_password_and_email(
            auth.email, auth.password.get_secret_value(), auth.aud.aud
        )
        return AuthTokenDTO.model_validate(dto)


class AuthUserWithRefreshToken(BaseAuthUsecase):
    async def __call__(self, auth: AuthTokenDTO):
        dto = await self.auth_service.auth_user_with_refresh_token(
            auth.accsess_token, auth.refresh_token
        )
        return AuthTokenDTO.model_validate(dto)


class AuthUserWithUpdateRole(BaseAuthUsecase):
    async def __call__(self, auth: UserRefreshTokenUpdatedDTO):
        dto = await self.auth_service.update_token_with_refresh_token(
            auth.user_id, auth.refresh_token, auth.aud.aud
        )
        return AuthTokenDTO.model_validate(dto)
