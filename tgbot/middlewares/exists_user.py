from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, CallbackQuery, Message

from tgbot.service.repo.repository import SQLAlchemyRepos
from tgbot.service.repo.user_repo import UserRepo


class ExistsUser(BaseMiddleware):

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: Message | CallbackQuery,
            data: Dict[str, Any]
    ) -> Any:
        telegram_user = event.from_user

        repo: SQLAlchemyRepos = data['repo']

        user = await repo.get_repo(UserRepo).get_user(telegram_user.id)
        if user is None:
            user = await repo.get_repo(UserRepo).add_user(
                telegram_user.id,
                telegram_user.first_name,
                telegram_user.last_name,
                telegram_user.username
            )
        data['user'] = user

        result = await handler(event, data)

        data.pop('user')
        return result
