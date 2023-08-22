from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.engine import URL

from settings import load_settings


class Base(DeclarativeBase):
    pass


settings = load_settings()
postgresql_url = URL.create(
    "postgresql+asyncpg",
    username=settings.db.user,
    password=settings.db.password,
    host=settings.db.host,
    port=settings.db.port,
    database=settings.db.name,
)


engine = create_async_engine(postgresql_url)
async_session = async_sessionmaker(engine, expire_on_commit=False)
