import uuid

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database.models import Audio


async def create_audiofile(db: AsyncSession, user_uuid: str, file_path: str):
    """Записывает аудио файл в базу данных c присвоением
       ему уникального идентификатора и uuid"""

    new_file = Audio(
        UUID=str(uuid.uuid4()),
        user_UUID=user_uuid,
        file_path=file_path,
    )
    db.add(new_file)
    await db.commit()
    return new_file


async def get_file(db: AsyncSession, file_id: str, user_id: str):
    """Получает и возвращает аудио файл из базы данных
       или возвращает None если файла нет"""
    stmt = select(Audio).where(Audio.UUID == file_id,
                               Audio.user_UUID == user_id)
    file = await db.execute(stmt)
    return file.scalar()
