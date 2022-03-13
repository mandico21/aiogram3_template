from aiogram import types
from aiogram.dispatcher.filters import BaseFilter
from aiogram.types import Message, CallbackQuery

from tgbot.service.repo.repository import SQLAlchemyRepos
from tgbot.service.repo.user_repo import UserRepo


class UserIsAdmin(BaseFilter):

    async def __call__(self, obj: Message | CallbackQuery, event_from_user: types.User, repo: SQLAlchemyRepos) -> bool:
        admin = await repo.get_repo(UserRepo).get_user(telegram_id=event_from_user.id)
        if not admin.is_admin:
            return True
        return False
