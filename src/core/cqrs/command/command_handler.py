from src.core.ports import Dependencies
from src.core.ports.command import CommandHandlerFactory
from src.core.cqrs.command import CreateCommand
from src.core.usecase.user_usecase import CreateUserUsecase

command_router = CommandHandlerFactory()

dep: Dependencies = {
    "usecase": CreateUserUsecase
}
@command_router.command_handler()
async def handle_create_user(type_command=CreateCommand(), dependencies=dep):
    dependencies["usecase"]()