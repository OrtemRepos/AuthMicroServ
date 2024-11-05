from pydantic_settings import BaseSettings


class JWTsettings(BaseSettings):
    secret_key: str = "1"
    algorithms: list[str] = ["1"]
    access_token_expire_ms: int = 3_600_000
    refresh_token_size: int = 1


class ThreadPoolExecutorSettings(BaseSettings):
    max_worker: int = 1


class LruCacheRouter(BaseSettings):
    max_size_command_router: int = 20
    max_size_query_router: int = 20


class RedisSettings(BaseSettings):
    redis_url: str = "redis://localhost"
    refresh_token_expire_ms: int = 3_600_000 * 24 * 30


class Settings(BaseSettings):
    jwt_settings: JWTsettings = JWTsettings()
    thread_poll_settings: ThreadPoolExecutorSettings = (
        ThreadPoolExecutorSettings()
    )
    ltu_cache: LruCacheRouter = LruCacheRouter()


settings = Settings()
