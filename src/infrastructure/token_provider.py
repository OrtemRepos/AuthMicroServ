import jwt
import secrets
from typing import Protocol
from abc import abstractmethod
from uuid import UUID
from time import time
from src.config import JWTsettings
from src.core.domain.entities.value_objects import (
    ID,
    AccsesToken,
    TokenPayload,
)
from src.core.domain.entities import RefreshToken


class TokenProviderInterface(Protocol):
    settings: JWTsettings

    @abstractmethod
    def generate_token(self, user_id: ID, aud: str, role_ids: set[int]) -> AccsesToken:
        pass

    @abstractmethod
    def generate_refresh_token(self, user_id: ID) -> RefreshToken:
        pass

    @abstractmethod
    def decode(self, token: AccsesToken) -> TokenPayload:
        pass


class TokenProvider:
    def __init__(self, settings: JWTsettings) -> None:
        self.settings: JWTsettings = settings

    def _generate_payload(
        self, user_id: UUID, aud: str, role_ids: set[int]
    ) -> TokenPayload:
        payload = TokenPayload(
            sub=str(user_id),
            aud=aud,
            exp=self.settings.access_token_expire_ms + int(time() * 1000),
            roles=role_ids,
        )
        return payload

    def generate_token(
        self, user_id: UUID, aud: str, role_ids: set[int]
    ) -> AccsesToken:
        token = jwt.encode(
            payload=self._generate_payload(user_id, aud, role_ids).model_dump(),
            key=self.settings.secret_key,
            algorithm=self.settings.algorithms[0],
        )
        return AccsesToken(value=token)

    def generate_refresh_token(self, user_id: ID) -> RefreshToken:
        return RefreshToken(
            id=user_id, token=secrets.token_urlsafe(self.settings.refresh_token_size)
        )

    def decode(self, token: AccsesToken) -> TokenPayload:
        decode = jwt.decode(
            jwt=token.value,
            key=self.settings.secret_key,
            algorithms=self.settings.algorithms,
        )
        payload = TokenPayload(**decode)
        return payload
