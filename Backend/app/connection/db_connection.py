from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio.engine import AsyncEngine
from app.config.app_config import AppConfig
from sqlmodel import SQLModel, TEXT


database_engine = AsyncEngine(
    create_engine(
        url=AppConfig.DATABASE_URL,
        echo=True,
        future=True
    )
)

# checking if the database exits here

# we will attempt to create the psych engine here
async def db_init():
    from app.models.auth.User import User
    async with database_engine.connect() as conn:
        if conn:
            await conn.run_sync(SQLModel.metadata.create_all)
        else:
            await conn.close()
