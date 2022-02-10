from aiogram import Router
from aiogram.dispatcher.filters.command import CommandStart
from aiogram.types import Message

welcome_router = Router()


@welcome_router.message(CommandStart())
async def on_start_command(msg: Message) -> None:
    await msg.answer(f'Здравствуйте, {msg.from_user.full_name}')


@welcome_router.message(commands='help')
async def on_help_command(msg: Message) -> None:
    await msg.answer("Помощь")
