from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio.engine import AsyncEngine
from sqlalchemy.orm.session import sessionmaker
from sqlmodel.ext.asyncio.session import AsyncSession
from app.config.app_config import AppConfig
from sqlmodel import SQLModel, TEXT


database_engine = AsyncEngine(
    create_engine(
        url=AppConfig.DATABASE_URL,
        echo=True,
        future=True
    )
)


# we will attempt to create the psych engine here
async def db_init():
    async with database_engine.connect() as conn:
        if conn:
            await conn.run_sync(SQLModel.metadata.create_all)
        else:
            await conn.close()


# the function to get the session here for the
# different services already defined
async def get_session() -> AsyncSession:
    Session = sessionmaker(
        bind=database_engine,
        expire_on_commit=False,
        class_=AsyncSession
    )

    async with Session() as session:
        yield session
