from fastapi import FastAPI

from app.api.v1.routers import main_router

app = FastAPI(title='Library API')

app.include_router(main_router)
