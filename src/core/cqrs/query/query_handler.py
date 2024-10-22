from src.core.ports.query.query import QueryHandlerFactory
from src.core.domain.entities.aggregates.user_aggregate import UserAggregate
from src.core.domain.cqrs.query import GetByIdQuery


factory = QueryHandlerFactory()


@factory.query_handler()
async def get_by_id(type_query: GetByIdQuery, domain_entity: UserAggregate):
    pass
