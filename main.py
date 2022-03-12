import asyncio
import logging

from logs.logger_conf import setup_logging
from tgbot.bot import main

logger = logging.getLogger()


if __name__ == '__main__':
    try:
        setup_logging('logs/logger.yml')
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")
