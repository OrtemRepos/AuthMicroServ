from abc import ABC
from src.core.domain.service import AuthService
from src.core.domain.entities.value_objects import AccsesToken, RefreshToken


class BaseAuthUsecase(ABC):
    def __init__(self, auth_service: AuthService) -> None:
        self.auth_service = auth_service


class AuthUserWithPassword(BaseAuthUsecase):
    def __call__(self, email: str, password: str, aud: str):
        return self.auth_service.auth_user_with_password_and_email(email, password, aud)


class AuthUserWithRefreshToken(BaseAuthUsecase):
    def __call__(self, accses_token: AccsesToken, refresh_token: RefreshToken):
        return self.auth_service.auth_user_with_refresh_token(
            accses_token, refresh_token
        )


class AuthUserWithUpdateRole(BaseAuthUsecase):
    def __call__(self, accses_token: AccsesToken, refresh_token: RefreshToken):
        return self.auth_service.update_token_with_refresh_token(
            accses_token, refresh_token
        )
