from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault, BotCommandScopeChat

from tgbot.config import Config


async def set_commands(
        bot: Bot,
        config: Config
) -> None:
    commands = [
        BotCommand(
            command="start",
            description="Запустить бота 🟢"
        ),
        BotCommand(
            command="help",
            description="Вывести справку 📃"
        ),
    ]
    await bot.set_my_commands(commands=commands, scope=BotCommandScopeDefault())
    for admin in config.tg_bot.admin_ids:
        commands.append(
            BotCommand(
                command="check",
                description="Проверить статус ⚡"
            )
        )
        await bot.set_my_commands(commands=commands, scope=BotCommandScopeChat(chat_id=admin))
