from app.core.db import Base, engine
from contextlib import asynccontextmanager


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@asynccontextmanager
async def get_db_context():
    async with engine.begin() as conn:
        yield conn