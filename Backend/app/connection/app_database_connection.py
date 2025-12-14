from sqlalchemy import create_engine
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio.engine import AsyncEngine
from ..config.project_config import ProjectConfig
from typing import Text
from sqlmodel import select, SQLModel


# the main app engine will be here
main_app_engine = AsyncEngine(
    create_engine(
        url=ProjectConfig.DATABASE_URL,
        echo=True
    )
)


# establishing the database connection here
async def database_init():
    async with main_app_engine.begin() as connection:
        from ..models.products.product_model import ProductModel
        await connection.run_sync(SQLModel.metadata.create_all)
