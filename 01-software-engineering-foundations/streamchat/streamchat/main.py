from fastapi import FastAPI

from routes import router

app = FastAPI(
    title="StreamChat"
)

app.include_router(router)