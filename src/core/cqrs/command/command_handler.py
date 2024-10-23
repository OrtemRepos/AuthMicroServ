from src.core.ports.command import CommandHandlerRouter
from src.core.cqrs.command import CreateCommand, UpdateCommand, DeleteCommand
from src.core.usecase import UsecaseType

command_router = CommandHandlerRouter()


@command_router.command_handler()
async def handle_create(command_type: CreateCommand, usecase_type: UsecaseType):
    await usecase_type(command_type.dto)  # type: ignore


@command_router.command_handler()
async def handle_update(command_type: UpdateCommand, usecase_type: UsecaseType):
    await usecase_type(command_type.id, command_type.dto)  # type: ignore


@command_router.command_handler()
async def handle_delete(command_type: DeleteCommand, usecase_type: UsecaseType):
    await usecase_type(command_type.id)  # type: ignore


for i, k in command_router._handlers_factory.items():
    print(f"{i} - {k}")
