import uuid
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
import random
from string import ascii_letters
from database.models import User
from schemas import UserCreate
from utils.functions import unique_string_generator


async def create_user(db: AsyncSession, user: UserCreate):
    """Записывает пользователя в базу данных c присвоением
       ему уникального идентификатора и uuid"""

    new_user = User(
        name=user.name,
        unique_slug=unique_string_generator(),
        UUID=str(uuid.uuid4()),
    )
    db.add(new_user)
    await db.commit()
    return new_user


async def get_user(db: AsyncSession, slug: str, uuid: str):
    """Получает и возвращает пользователя из базы данных
       или возвращает None если файла нет"""
    stmt = select(User).where(User.unique_slug == slug, User.UUID == uuid)
    user = await db.execute(stmt)
    return user.scalar()
