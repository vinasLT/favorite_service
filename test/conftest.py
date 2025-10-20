# tests/conftest.py
import asyncio
import pytest
from typing import AsyncGenerator

from httpx import AsyncClient, ASGITransport
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.pool import StaticPool

from app.database.db.session import get_async_db
from app.database.models import Base
from app.main import create_app

@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()

@pytest.fixture(scope="session")
def test_app():
    app = create_app()
    return app

@pytest.fixture(scope="session")
async def test_engine():
    # In-memory SQLite для скорости; если используешь Postgres — подставь свой URL тестовой БД
    url = "sqlite+aiosqlite:///:memory:"
    engine = create_async_engine(
        url,
        future=True,
        echo=False,
        poolclass=StaticPool,  # важно для in-memory
    )
    # здесь можно выполнить создание схемы, если у тебя есть metadata
    # from app.models import Base
    # async with engine.begin() as conn:
    #     await conn.run_sync(Base.metadata.create_all)

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield engine
    await engine.dispose()

@pytest.fixture()
async def db_session(test_engine) -> AsyncGenerator[AsyncSession, None]:
    async_session = async_sessionmaker(test_engine, class_=AsyncSession, expire_on_commit=False)
    async with test_engine.begin() as conn:
        # стартуем SAVEPOINT, чтобы потом откатить изменения теста
        trans = await conn.begin()
        session = async_session(bind=conn)
        try:
            yield session
        finally:
            await session.close()
            await trans.rollback()

@pytest.fixture()
async def client(test_app, db_session):
    # подменяем зависимость БД на тестовую сессию
    async def _override_db():
        yield db_session

    test_app.dependency_overrides[get_async_db] = _override_db

    transport = ASGITransport(app=test_app, raise_app_exceptions=True)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac

    test_app.dependency_overrides.clear()