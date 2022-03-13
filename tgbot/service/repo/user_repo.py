from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from tgbot.models.user import User
from tgbot.service.repo.base_repo import BaseSQLAlchemyRepo


class UserRepo(BaseSQLAlchemyRepo):
    model = User

    async def add_user(self,
                       telegram_id: int,
                       first_name: str,
                       last_name: str = None,
                       username: str = None) -> model:
        sql = insert(self.model).values(telegram_id=telegram_id,
                                        first_name=first_name,
                                        last_name=last_name,
                                        username=username).returning('*')
        result = await self._session.execute(sql)
        await self._session.commit()
        return result.first()

    async def get_user(self, telegram_id: int) -> model:
        sql = select(self.model).where(self.model.telegram_id == telegram_id)
        request = await self._session.execute(sql)
        user = request.scalar()
        return user
