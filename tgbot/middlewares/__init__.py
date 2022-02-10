from aiogram import Dispatcher

from tgbot.middlewares.throttling import ThrottlingMiddleware


def setup_middlwares(dp: Dispatcher):
    dp.message.middleware(ThrottlingMiddleware())
