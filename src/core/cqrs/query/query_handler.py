from src.core.ports.query import QueryRouter
from src.core.cqrs.query import (
    GetByIdQuery,
    AuthWithPasswordQuery,
    GetByNameQuery,
    AuthWithRefreshTokenQuery,
    AuthWithUpdateTokenQuery,
)
from src.core.usecase import (
    AuthUserWithPassword,
    AuthUserWithRefreshTokenUsecase,
    AuthUserWithUpdateRoleUsecase,
    GetPremissionUsecase,
    GetRoleUsecase,
    GetUserUsecase,
)

query_router: QueryRouter = QueryRouter()


query_router.register(
    handle_query=GetByIdQuery,
    handlers=[GetPremissionUsecase, GetRoleUsecase, GetUserUsecase],
)
query_router.register(
    handle_query=AuthWithPasswordQuery, handlers=[AuthUserWithPassword]
)
query_router.register(
    handle_query=GetByNameQuery,
    handlers=[GetPremissionUsecase, GetRoleUsecase, GetUserUsecase],
)
query_router.register(
    handle_query=AuthWithRefreshTokenQuery, handlers=[AuthUserWithRefreshTokenUsecase]
)
query_router.register(
    handle_query=AuthWithUpdateTokenQuery, handlers=[AuthUserWithUpdateRoleUsecase]
)
