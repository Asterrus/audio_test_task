import random
from string import ascii_letters

from fastapi import UploadFile
from pydub import AudioSegment

AudioSegment.converter = (r"C:\Users\Gastu\Desktop\ffmpeg-2023-05-18-git-01d9"
                          r"a84ef5-full_build\ffmpeg-2023-05-18-git-01d9a84ef"
                          r"5-full_build\bin\\ffmpeg.exe")

DIR = 'files/'


def to_mp3_converter(file: UploadFile, end_path: str) -> None:
    """Конвертирует входящий аудио файл в формат .mp3
     и записывает его по указанному в end_path пути"""
    song = AudioSegment.from_file_using_temporary_files(file.file)
    song.export(end_path, format="mp3")


def to_mp3_format_change(file_name: str) -> str:
    """Меняет формат файла на .mp3"""
    return file_name[:-4] + '.mp3'


def unique_string_generator(k: int) -> str:
    """генерирует уникальную строку"""
    return ''.join(random.choices(ascii_letters, k=k))
