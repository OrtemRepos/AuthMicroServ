# from src.infrastructure.command import CommandRouter
# from src.core.cqrs.command import UpdateCommand, DeleteCommand, CreateCommand
# from src.core.usecase import (
#     CreateRoleUsecase,
#     CreateUserUsecase,
#     CreatePremissionUsecase,
#     UpdatePremissionUsecase,
#     UpdateRoleUsecase,
#     UpdateUserUsecase,
#     DeletePremissionUsecase,
#     DeleteRoleUsecase,
#     DeleteUserUsecase,
# )

# router: CommandRouter = CommandRouter()


# router.register(
#     handle_command=CreateCommand,
#     handlers=[CreatePremissionUsecase, CreateRoleUsecase, CreateUserUsecase],
# )  # type: ignore
# router.register(
#     handle_command=UpdateCommand,
#     handlers=[UpdatePremissionUsecase, UpdateRoleUsecase, UpdateUserUsecase],
# )  # type: ignore
# router.register(
#     handle_command=DeleteCommand,
#     handlers=[DeletePremissionUsecase, DeleteRoleUsecase, DeleteUserUsecase],
# )  # type: ignore

# print(router._handlers)
