from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio.engine import AsyncEngine
from app.config.app_config import app_config
from sqlmodel import SQLModel, TEXT


database_engine = AsyncEngine(
    create_engine(
        url=app_config.SQLITE_DATABASE,
        echo=True
    )
)

# we will attempt to create the psych engine here
async def db_init():
    from app.models.auth.User import User
    async with database_engine.connect() as conn:
        await conn.execute(TEXT("SELECT 'hello world here'"))
