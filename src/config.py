from pydantic_settings import BaseSettings


class JWTsettings(BaseSettings):
    secret_key: str = "1"
    algorithms: list[str] = ["1"]
    access_token_expire_ms: int = 1
    refresh_token_expire_ms: int = 1
    refresh_token_size: int = 1


class ThreadPoolExecutorSettings(BaseSettings):
    max_worker: int = 1


class Settings(BaseSettings):
    jwt_settings: JWTsettings = JWTsettings()
    thread_poll_settings: ThreadPoolExecutorSettings = ThreadPoolExecutorSettings()


settings = Settings()
