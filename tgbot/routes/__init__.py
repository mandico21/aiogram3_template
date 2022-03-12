from aiogram import Dispatcher, Router, F

from tgbot.config import Config
from tgbot.routes.admin.admin_check import admin_check_router
from tgbot.routes.errors import errors_router
from tgbot.routes.welcome import welcome_router


def register_all_routes(dp: Dispatcher, config: Config) -> None:
    master_router = Router()
    admin_router = Router()
    dp.include_router(master_router)
    dp.include_router(errors_router)

    master_router.include_router(welcome_router)
    master_router.include_router(admin_router)
    # Administrator routers
    admin = config.tg_bot.admin_ids
    admin_check_router.message.filter(F.from_user.id.in_(admin))
    admin_router.include_router(admin_check_router)
