### Описание
   Тестовое задание. 
   <details><summary>Описание задания</summary>

      Необходимо реализовать веб-сервис, выполняющий следующие функции:
      1. Создание пользователя;
      2. Для каждого пользователя - сохранение аудиозаписи в формате wav, преобразование  
      её в формат mp3 и запись в базу данных и предоставление ссылки для скачивания аудиозаписи.

      Детализация задачи:

      1. С помощью Docker (предпочтительно - docker-compose) развернуть образ с любой опенсорсной СУБД (предпочтительно - PostgreSQL).  
      Предоставить все необходимые скрипты и конфигурационные (docker/compose) файлы для развертывания СУБД,
      а также инструкции для подключения к ней.  
      Необходимо обеспечить сохранность данных при рестарте контейнера
      то есть - использовать volume-ы для хранения файлов СУБД на хост-машине.  
      2. Реализовать веб-сервис со следующими REST методами:  
         2.1 Создание пользователя, POST:
            2.1.1 Принимает на вход запросы с именем пользователя;
            2.1.2 Создаёт в базе данных пользователя заданным именем, так же генерирует уникальный идентификатор пользователя  
            и UUID токен доступа (в виде строки) для данного пользователя;
            2.1.3 Возвращает сгенерированные идентификатор пользователя и токен.
         2.2 Добавление аудиозаписи, POST:
            2.2.1 Принимает на вход запросы, содержащие уникальный идентификатор пользователя, токен доступа и аудиозапись в формате wav;
            2.2.2 Преобразует аудиозапись в формат mp3, генерирует для неё уникальный UUID идентификатор и сохраняет их в базе данных;
            2.2.3 Возвращает URL для скачивания записи вида http://host:port/record?id=id_записи&user=id_пользователя.
         2.3 Доступ к аудиозаписи, GET:
            2.3.1 Предоставляет возможность скачать аудиозапись по ссылке из п 2.2.3.
      3. Для всех сервисов метода должна быть предусмотрена предусмотрена обработка различных ошибок,  
      возникающих при выполнении запроса, с возвращением соответствующего HTTP статуса.
      4. Модель данных (таблицы, поля) для каждого из заданий можно выбрать по своему усмотрению.
      5. В репозитории с заданием должны быть предоставлены инструкции по сборке докер-образа  
      с сервисами из пп. 2. и 3., их настройке и запуску. А также пример запросов к методам сервиса.
      6. Желательно, если при выполнении задания вы будете использовать docker-compose, SQLAlchemy,  пользоваться аннотацией типов.


   </details>  
   
   Реализован веб сервис на FastAPI, с возможностью создания пользователей и конвертацией wav файлов в mp3.  
   База данных - PostgreSQL  
   ORM - SQLAlchemy, миграции - Alembic  
   Проект разворачивается с помощью docker compose  
   Python версии 3.11.1  
   Для конвертации аудио файлов используются FFmpeg и pydub.  
### Технологии:
![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![FastAPI](https://img.shields.io/badge/FastAPI-092E20?style=for-the-badge&logo=FastAPI&logoColor=green)
![Docker](https://img.shields.io/badge/Docker-092E20?style=for-the-badge&logo=docker&logoColor=blue)
![FFmpeg](https://img.shields.io/badge/FFmpeg-092E20?style=for-the-badge&logo=FFmpeg&logoColor=green)
### Используемые пакеты:
* fastapi==0.95.2
* asyncpg==0.27.0  
* httpx==0.24.0  
* uvicorn==0.22.0  
* SQLAlchemy==2.0.13  
* alembic==1.11.0  
* python-dotenv==1.0.0  
* python-multipart==0.0.6
* aiofiles==23.1.0
* pydub==0.25.1

### Установка

1. Клонировать репозиторий:

   ```python
   git clone ...
   ```

2. Перейти в папку с проектом:

   ```python
   cd audio_test_task/
   ```

3. Создать и запустить контейнер:

   ```python
   docker-compose up -d
   ```

4. (Опционально) Панель управления pgadmin доступна по адресу http://localhost:5050/  
    Авторизация:  
    email=pgadmin4@pgadmin.org  
    password=admin  
    Подключение к базе:  
    1.  
    ![image](https://github.com/Asterrus/quize_test_task/assets/59145527/550ec784-0231-46cc-a50d-f3a9b937cff7)   
    2.  
    ![image](https://github.com/Asterrus/quize_test_task/assets/59145527/61eb020e-64f8-4c87-b936-4afe72274dba)   
    3.  
    ![image](https://github.com/Asterrus/quize_test_task/assets/59145527/b6a463f2-d25c-46c9-823d-7ca60c623b2a)   

### Дополнительно

* Ресурс доступен по адресу:
   ```
   http://localhost:8000/
   ```

* Документация:
   ```
   http://localhost:8000/docs
   ```
### Пример запроса
* Добавление пользователя в базу данных. возвращает уникальный идентификатор и UUID токен доступа.
    `POST http://localhost:8000/users/sign_up`
* Пример запроса:
    ```json
    {
      "name": "Jack"
    }
    ```
* Пример ответа:
    ```json
    {
      "unique_slug": "JackwSdROFNRyo",
      "UUID": "cc7a7d33-f36f-4cdd-87b5-067748624511"
    }
    ```
* Загрузка и конвертация файла.  
    `POST http://localhost:8000/upload_file/`
* Пример запроса:
    ```
    curl -X 'POST' \
    'http://localhost:8000/upload_file/' \
    -H 'accept: application/json' \
    -H 'Content-Type: multipart/form-data' \
    -F 'file=@sample-3s.wav;type=audio/wav' \
    -F 'slug=JackwSdROFNRyo' \
    -F 'uuid=cc7a7d33-f36f-4cdd-87b5-067748624511'
    ```
* Пример ответа:
    ```json
    {
      "Ссылка на файл": "http://localhost:8000/record?id=fdd8149c-a329-42cd-af17-335db4a87a88&user=cc7a7d33-f36f-4cdd-87b5-067748624511"
    }
    ```
* Скачивание файла:  
  `GET http://localhost:8000/record?id=fdd8149c-a329-42cd-af17-335db4a87a88&user=cc7a7d33-f36f-4cdd-87b5-067748624511`  
  В теле ответа будет содержаться файл mp3.  
### Автор проекта 
* Роман Дячук   


