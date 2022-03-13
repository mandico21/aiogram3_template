from sqlalchemy import BigInteger, Column, String, Boolean

from tgbot.models.base import BaseModel


class User(BaseModel):
    __tablename__ = 'users'

    telegram_id = Column(BigInteger, nullable=False, autoincrement=False, primary_key=True)
    first_name = Column(String(length=60), nullable=False)
    last_name = Column(String(length=60), nullable=True)
    username = Column(String(length=100), nullable=True)
    is_admin = Column(Boolean(), default=False)

    def __repr__(self):
        return f'User (ID: {self.telegram_id} - {self.first_name} {self.last_name})'
