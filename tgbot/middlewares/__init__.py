from aiogram import Dispatcher

from tgbot.middlewares.log_update import LogUpdatesMiddleware
from tgbot.middlewares.throttling import ThrottlingMiddleware


def setup_middlwares(dp: Dispatcher):
    dp.message.middleware(ThrottlingMiddleware())
    dp.message.outer_middleware(LogUpdatesMiddleware())
    dp.callback_query.outer_middleware(LogUpdatesMiddleware())
