import asyncio
import logging

from logs.logger_conf import setup_logging
from tgbot.bot import on_startup

logger = logging.getLogger()


if __name__ == '__main__':
    try:
        setup_logging('logs/logger.yml')
        asyncio.run(on_startup())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")
