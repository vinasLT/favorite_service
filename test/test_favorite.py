import pytest
from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession


@pytest.mark.asyncio
async def test_create_favorite(test_app: FastAPI, db_session: AsyncSession):
    pass
