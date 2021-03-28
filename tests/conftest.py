import warnings

import pytest
import docker as libdocker
from asgi_lifespan import LifespanManager
from fastapi import FastAPI
from httpx import AsyncClient


@pytest.fixture(scope="session")
def docker() -> libdocker.APIClient:
    with libdocker.APIClient(version="auto") as client:
        yield client


@pytest.fixture(scope="session", autouse=True)
def mariadb_server(docker: libdocker.APIClient) -> None:
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    yield
    return

# @pytest.fixture(autouse=True)
# async def apply_migrations(mariadb_server: None) -> None:
#     alembic.config.main(argv=["upgrade", "head"])
#     yield
#     alembic.config.main(argv=["downgrade", "base"])


@pytest.fixture
# def app(apply_migrations: None) -> FastAPI:
def app(mariadb_server: None) -> FastAPI:
    from app.main import app  # local import for testing purpose
    return app


@pytest.fixture
async def initialized_app(app: FastAPI) -> FastAPI:
    async with LifespanManager(app):
        yield app


# @pytest.fixture
# def pool(initialized_app: FastAPI) -> Pool:
#     return initialized_app.state.pool


@pytest.fixture
async def client(initialized_app: FastAPI) -> AsyncClient:
    async with AsyncClient(
        app=initialized_app,
        base_url="http://localhost",
        headers={"Content-Type": "application/json"},
    ) as client:
        yield client
