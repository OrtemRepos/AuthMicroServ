from collections.abc import Coroutine
from typing import Any

from src.core.domain.entities import RefreshToken
from src.core.domain.entities.value_objects import ID, AccsesToken
from src.core.domain.service.token_service import TokenService
from src.core.domain.service.user_service import UserService


class AuthService:
    def __init__(
        self, token_service: TokenService, user_service: UserService
    ) -> None:
        self.token_service = token_service
        self.user_service = user_service

    async def auth_user_with_password_and_email(
        self, email: str, password: str, aud: str
    ) -> tuple[AccsesToken, RefreshToken]:
        user = await self.user_service.get_auth_user(
            email=email, password=password
        )
        refresh_token = await self.token_service.create_refresh_token(
            user_id=user.user_id
        )
        accses_token = self.token_service.create_accses_token(
            user_id=user.user_id, aud=aud, role_ids=user.role_ids
        )
        return accses_token, refresh_token

    async def auth_user_with_refresh_token(
        self, accses_token, refresh_token: RefreshToken
    ) -> tuple[AccsesToken, Coroutine[Any, Any, RefreshToken]]:
        server_refresh_token = (
            await self.token_service.get_refresh_token_by_token(refresh_token)
        )
        if server_refresh_token:
            return await self.token_service.refresh_accses_token(
                accses_token=accses_token
            )
        raise ValueError(f"{refresh_token=} not valid")

    async def update_token_with_refresh_token(
        self, user_id: ID, refresh_token: RefreshToken, aud: str
    ) -> tuple[AccsesToken, RefreshToken]:
        user = await self.user_service.get_user_by_id(user_id)
        if user:
            refresh_token = await self.token_service.create_refresh_token(
                user_id=user.user_id
            )
            accses_token = self.token_service.create_accses_token(
                user_id=user.user_id, aud=aud, role_ids=user.role_ids
            )
            return accses_token, refresh_token
        raise ValueError(f"Not valid {user_id=}")
