from fastapi import APIRouter

from database.crud.user import create_user
from database.db import database
from schemas import UserCreate, UserSecretsOut


user_router = APIRouter(
    tags=['user'],
    prefix='/users'
)


@user_router.post('/sign_up', response_model=UserSecretsOut)
async def sign_up(db: database, user: UserCreate):
    """Создания пользователя"""
    return await create_user(db, user)

