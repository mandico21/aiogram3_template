import logging

from aiogram import Router
from aiogram.exceptions import TelegramAPIError
from aiogram.types import Update

logger = logging.getLogger(__name__)
errors_router = Router()


@errors_router.errors()
async def errors_handler(update: Update, exception: TelegramAPIError):
    logger.exception(
        f"{str(exception)}.\n"
        f"Update: {update.dict()}"
    )
