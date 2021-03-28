import pytest
from fastapi import FastAPI
from httpx import AsyncClient
from starlette.status import HTTP_404_NOT_FOUND, HTTP_405_METHOD_NOT_ALLOWED

pytestmark = pytest.mark.asyncio


async def test_wrong_path(app: FastAPI):
    async with AsyncClient(base_url="http://localhost", app=app) as client:
        response = await client.get("/wrong_path/asd")
        assert response.status_code == HTTP_404_NOT_FOUND
        error_data = response.json()
        assert 'detail' in error_data
        assert error_data['detail'] == 'Not Found'


async def test_method_not_allowed(app: FastAPI):
    async with AsyncClient(base_url="http://localhost", app=app) as client:
        response = await client.get(
            app.url_path_for('couriers:post_create_courier')
        )
        assert response.status_code == HTTP_405_METHOD_NOT_ALLOWED
        error_data = response.json()
        assert 'detail' in error_data
        assert error_data['detail'] == 'Method Not Allowed'
