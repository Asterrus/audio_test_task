from fastapi import HTTPException, status


class UserNotFoundException(HTTPException):
    def __init__(self):
        self.detail = 'Пользователь с данными unique_slug и UUID не найден'
        self.status_code = status.HTTP_404_NOT_FOUND


class FileFormatException(HTTPException):
    def __init__(self):
        self.detail = 'Допускаются только файлы с разрешением wav'
        self.status_code = status.HTTP_400_BAD_REQUEST


class ConvertationException(HTTPException):
    def __init__(self, err):
        self.detail = f'Ошибка во время конвертирования файла:{err}'
        self.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR


class FileNotFoundException(HTTPException):
    def __init__(self):
        self.detail = 'Аудио файл с указанными id и user_id не найден'
        self.status_code = status.HTTP_404_NOT_FOUND

