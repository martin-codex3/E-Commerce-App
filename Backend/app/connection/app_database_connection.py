from sqlalchemy import create_engine
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio.engine import AsyncEngine
from ..config.project_config import ProjectConfig
from typing import Text
from sqlmodel import select

main_app_engine = AsyncEngine(
    create_engine(
        url=ProjectConfig.DATABASE_URL,
        echo=True
    )
)


# establishing the database connection here
async def database_init():
    async with main_app_engine.begin() as connection:
        print("We are going to inject the tables here")