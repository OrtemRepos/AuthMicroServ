import socket
from uuid import UUID
from pydantic import BaseModel, ConfigDict, Field

type ID = UUID | int


class ValueObject(BaseModel):
    model_config = ConfigDict(frozen=True)


class AccsesToken(ValueObject):
    value: str = Field(examples=["JWT token"], description="Accses Token jwt")


class TokenPayload(ValueObject):
    iss: str = Field(
        default_factory=lambda: socket.gethostbyname(socket.gethostname()),
        examples=["auth-serv-127.0.0.1"],
        description="Issuer",
    )
    sub: str = Field(examples=["user-1", "user-2", "user-3"], description="Subject")
    aud: str = Field(examples=["127.0.0.1"], description="Audience server")
    exp: int = Field(examples=[3600], description="Expiration time in milliseconds")
    roles: set[int] = Field(examples=["admin", "user"], description="List of roles")
