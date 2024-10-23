from src.core.ports.query import QueryHandlerRouter
from src.core.cqrs.query import GetByIdQuery
from src.core.usecase import UsecaseType


factory = QueryHandlerRouter()


@factory.query_handler()
async def get_by_id(query_type: GetByIdQuery, usecase_type: UsecaseType):
    return await usecase_type(query_type.dto)  # type: ignore
