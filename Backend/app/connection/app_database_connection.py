from sqlalchemy import create_engine
from sqlmodel.ext.asyncio.session import AsyncSession

from app.config.app_config import AppConfig
from sqlalchemy.ext.asyncio.engine import AsyncEngine
from sqlmodel import SQLModel
from sqlalchemy.orm.session import sessionmaker


# creating the database engine here
async_database_engine = AsyncEngine(
    create_engine(
        url=AppConfig.DATABASE_URL,
        echo=True
    )
)

# initializing the database here
async def database_init():
    async with async_database_engine.begin() as connection:
        await connection.run_sync(SQLModel.metadata.create_all)


# using the session maker to create the app session
async def get_app_session():
    Session = sessionmaker(
        bind=async_database_engine,
        class_=AsyncSession,
        expire_on_commit=False
    )

    async with Session() as session:
        yield session