import logging

from aiogram import Bot, Dispatcher
from aiogram.dispatcher.fsm.storage.memory import MemoryStorage

from tgbot.config import Config, load_config
from tgbot.misc.bot_commands import set_commands
from tgbot.routes import register_all_routes

logger = logging.getLogger(__name__)


async def on_startup():
    config: Config = load_config('.env')
    bot = Bot(token=config.tg_bot.token, parse_mode='HTML')

    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)

    register_all_routes(dp, config)
    await set_commands(bot, config)
    try:
        logger.info('Starting bot')
        await bot.get_updates(offset=-1)
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    finally:
        await storage.close()
        await bot.session.close()
