import logging

from aiogram import Bot, Dispatcher
from aiogram.dispatcher.fsm.storage.memory import MemoryStorage
from aiogram.dispatcher.fsm.storage.redis import RedisStorage
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from tgbot.config import Config, load_config
from tgbot.middlewares import setup_middlwares
from tgbot.misc.bot_commands import set_commands
from tgbot.misc.req_func import make_connection_string
from tgbot.routes import register_all_routes

logger = logging.getLogger(__name__)


async def main():
    config: Config = load_config('.env')
    bot = Bot(token=config.tg_bot.token, parse_mode='HTML')

    engine = create_async_engine(
        make_connection_string(config.db), future=True, echo=False
    )

    session_fabric = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

    storage = RedisStorage.from_url(f"redis://{config.redis.host}") if config.tg_bot.use_redis else MemoryStorage()
    dp = Dispatcher(storage=storage)

    setup_middlwares(dp, session_fabric)

    register_all_routes(dp, config)
    await set_commands(bot, config)
    try:
        logger.info('Starting bot')
        await bot.get_updates(offset=-1)
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    finally:
        await storage.close()
        await bot.session.close()
