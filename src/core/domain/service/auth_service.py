from src.core.domain.service.token_service import TokenService
from src.core.domain.service.user_service import UserService

from src.core.domain.entities.value_objects import ID, AccsesToken, RefreshToken


class AuthService:
    def __init__(self, token_service: TokenService, user_service: UserService) -> None:
        self.token_service = token_service
        self.user_service = user_service

    async def auth_user_with_password_and_email(
        self, email: str, password: str, aud: str
    ) -> tuple[AccsesToken, RefreshToken]:
        user = await self.user_service.get_auth_user(email=email, password=password)
        if user:
            refresh_token = await self.token_service.create_refresh_token(
                user_id=user.entity.id
            )
            accses_token = self.token_service.create_accses_token(
                user_id=user.entity.id, aud=aud
            )
            return accses_token, refresh_token

    async def auth_user_with_refresh_token(
        self, accses_token, refresh_token: RefreshToken
    ) -> tuple[AccsesToken, RefreshToken]:
        return await self.token_service.refresh_accses_token(
            accses_token=accses_token, refresh_token=refresh_token
        )

    async def update_token_with_refresh_token(
        self, user_id: ID, aud: str, refresh_token: RefreshToken
    ) -> tuple[AccsesToken, RefreshToken]:
        user = self.user_service.get_user_by_id(user_id)
        payload = self.token_service.create_accses_token(user_id, aud, user.role_ids)
        if user:
            refresh_token = await self.token_service.create_refresh_token(
                user_id=user.entity.id
            )
            accses_token = self.token_service.create_accses_token(
                user_id=user.entity.id, aud=payload.aud
            )
            return accses_token, refresh_token
