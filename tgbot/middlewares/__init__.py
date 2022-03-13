from aiogram import Dispatcher, Router
from sqlalchemy.orm import sessionmaker

from tgbot.middlewares.db_session import DBSession
from tgbot.middlewares.exists_user import ExistsUser
from tgbot.middlewares.repo import Repository
from tgbot.middlewares.throttling import ThrottlingMiddleware


def setup_middlwares(dp: Dispatcher, sm: sessionmaker):
    dp.message.outer_middleware(DBSession(sm))
    dp.callback_query.outer_middleware(DBSession(sm))

    dp.message.outer_middleware(Repository())
    dp.callback_query.outer_middleware(Repository())

    dp.message.outer_middleware(ExistsUser())
    dp.callback_query.outer_middleware(ExistsUser())

    dp.message.middleware(ThrottlingMiddleware())
