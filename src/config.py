from pydantic_settings import BaseSettings


class JWTsettings(BaseSettings):
    secret_key: str
    algorithms: list[str]
    access_token_expire_ms: int
    refresh_token_expire_ms: int
    refresh_token_size: int


class ThreadPoolExecutorSettings(BaseSettings):
    max_worker: int


class Settings(BaseSettings):
    jwt_settings: JWTsettings = JWTsettings()
    thread_poll_settings: ThreadPoolExecutorSettings = ThreadPoolExecutorSettings()


settings = Settings()
