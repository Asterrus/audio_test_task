from fastapi import APIRouter
from typing import Annotated
from fastapi import File, UploadFile, Form, Request
from fastapi.responses import FileResponse
from database.crud.audio import create_audiofile, get_file
from database.crud.user import get_user
from database.db import database
from database.models import Audio
from utils.exceptions import (UserNotFoundException, FileFormatException,
                              FileNotFoundException, ConvertationException)
from utils.functions import to_mp3_converter, to_mp3_format_change, \
    unique_string_generator
from schemas import AudioBase
MEDIA_DIR = 'files/'

audio_router = APIRouter(
    tags=['audio'],
)


@audio_router.post("/upload_file/")
async def upload_file(db: database, request: Request,
                      file: Annotated[UploadFile, File()],
                      slug: Annotated[str, Form()],
                      uuid: Annotated[str, Form()]):
    """Загрузка аудио файла на сервер. Допускается только wav формат"""
    user = await get_user(db, slug, uuid)
    if not user:
        raise UserNotFoundException
    if not file.filename.endswith('.wav'):
        raise FileFormatException
    try:
        file.filename = unique_string_generator(10) + file.filename
        new_format = to_mp3_format_change(file.filename)
        to_mp3_converter(file, MEDIA_DIR+new_format)
        audio_file = await create_audiofile(db, uuid, MEDIA_DIR+new_format)
    except Exception as err:
        raise ConvertationException(err)
    finally:
        await file.close()

    return {"Ссылка на файл": (f"{request.base_url}record?id={audio_file.UUID}"
                               f"&user={audio_file.user_UUID}")}


@audio_router.get("/record")
async def download_file(db: database, audio: AudioBase) -> FileResponse:
    """Скачивание файла с сервера"""
    file: Audio = await get_file(db, audio.UUID, audio.user_UUID)
    if not file:
        raise FileNotFoundException
    return FileResponse(file.file_path)
