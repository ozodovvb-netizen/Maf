"""
PostgreSQL bilan async ulanish va session factory.
"""
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

from config import DATABASE_URL
from database.models import Base

_engine_kwargs = {"echo": False}
if DATABASE_URL.startswith("postgresql"):
    _engine_kwargs.update(pool_size=10, max_overflow=20)

engine = create_async_engine(DATABASE_URL, **_engine_kwargs)

async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def init_db():
    """Bot birinchi marta ishga tushganda barcha jadvallarni yaratadi."""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
