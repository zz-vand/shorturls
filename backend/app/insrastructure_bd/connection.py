from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from app.persistent_db.db import Base

#база - shorturls, пользователь - user_url, пароль - user_url
host_db = "db"
password_db = "user_url"
user_db = "user_url"
name_db = "shorturls"
port_db = 5432


DATABASE_URL_ASYNC = f"postgresql+asyncpg://{user_db}:{password_db}@{host_db}/{name_db}"
DATABSE_URL_SYNC = f"postgresql+psycopg://{user_db}:{password_db}@{host_db}/{name_db}"

def async_connection() -> async_sessionmaker[AsyncSession]:
    engine = create_async_engine(url=DATABASE_URL_ASYNC)
    return async_sessionmaker(autocommit = False, autoflush=False, bind = engine)

def create_all() -> None:
    engine = create_engine(url=DATABSE_URL_SYNC)
    Base.metadata.create_all(engine)
