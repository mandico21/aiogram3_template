from aiogram import Router
from aiogram.types import Message

admin_check_router = Router()


@admin_check_router.message(commands='check')
async def on_check_admin(msg: Message) -> None:
    await msg.reply('У Вас есть статус администратора')
