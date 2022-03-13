from sqlalchemy import Column, DateTime, func
from sqlalchemy.orm import declarative_base

Base = declarative_base()
metadata = Base.metadata


class BaseModel(Base):
    __abstract__ = True

    created_at = Column(DateTime(True), server_default=func.now())
    updated_at = Column(DateTime(True), default=func.now(), onupdate=func.now(), server_default=func.now())
