from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.core import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield


app = FastAPI(title="Electronic Library API", lifespan=lifespan)


@app.get("/health")
async def health():
    return {"status": "ok"}

