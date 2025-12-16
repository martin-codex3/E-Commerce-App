from sqlalchemy import create_engine

from app.config.app_config import AppConfig
from sqlalchemy.ext.asyncio.engine import AsyncEngine


# creating the database engine here
async_database_engine = AsyncEngine(
    create_engine(
        url=AppConfig.DATABASE_URL,
        echo=True
    )
)


# initializing the database here
