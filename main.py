from fastapi import FastAPI

from routers.audio import audio_router
from routers.user import user_router

app = FastAPI()
app.include_router(user_router)
app.include_router(audio_router)


