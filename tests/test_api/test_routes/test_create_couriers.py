import pytest
from fastapi import FastAPI
from httpx import AsyncClient
from starlette.status import (
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST
)

pytestmark = pytest.mark.asyncio


async def test_create_courier(app: FastAPI, client: AsyncClient):
    couriers_data = {
        "data": [
            {
                "courier_id": 1,
                "courier_type": "foot",
                "regions": [1, 12, 22],
                "working_hours": ["11:35-14:05", "09:00-11:00"]
            },
            {
                "courier_id": 2,
                "courier_type": "bike",
                "regions": [22],
                "working_hours": ["09:00-18:00"]
            },
            {
                "courier_id": 3,
                "courier_type": "car",
                "regions": [12, 22, 23, 33],
                "working_hours": []
            }
        ]
    }
    response = await client.post(
        app.url_path_for('couriers:post_create_courier'),
        json=couriers_data)
    assert response.status_code == HTTP_201_CREATED
    data = response.json()
    assert 'couriers' in data
    assert data == {
        "couriers": [{
            "id": 1
        }, {
            "id": 2
        }, {
            "id": 3
        }]
    }


async def test_cant_create_couriers_dublicates(
    app: FastAPI, client: AsyncClient
):
    couriers_data = {
        "data": [
            {
                "courier_id": 1,
                "courier_type": "foot",
                "regions": [1, 12, 22],
                "working_hours": ["11:35-14:05", "09:00-11:00"]
            },
            {
                "courier_id": 2,
                "courier_type": "bike",
                "regions": [22],
                "working_hours": ["09:00-18:00"]
            },
            {
                "courier_id": 4,
                "courier_type": "car",
                "regions": [12, 22, 23, 33],
                "working_hours": []
            }
        ]
    }
    response = await client.post(
        app.url_path_for('couriers:post_create_courier'),
        json=couriers_data)
    assert response.status_code == HTTP_400_BAD_REQUEST
    data = response.json()
    assert 'validation_error' in data
    assert data == {
        "validation_error": {
            "couriers": [{"id": 1}, {"id": 2}]
        }
    }


async def test_cant_create_courier_invalid_data(
    app: FastAPI, client: AsyncClient
):
    couriers_data = {
        "data": [
            {
                "courier_id": 1,
                "courier_type": "foot3",
                "regions": [1, 12, 22],
                "working_hours": ["11:35-14:05", "09:00-11:00"]
            },
            {
                "courier_id": 2,
                "courier_type": "bike",
                "regions": [22],
                "working_hours": ["09:00-28:00"]
            },
            {
                "courier_id": 3,
                "courier_type": "car",
                "regions": [12, 'wrong_data', 23, 33],
                "working_hours": []
            }
        ]
    }
    response = await client.post(
        app.url_path_for('couriers:post_create_courier'),
        json=couriers_data)
    assert response.status_code == HTTP_400_BAD_REQUEST
    data = response.json()
    assert 'validation_error' in data
    assert data == {
        "validation_error": {
            "couriers": [{"id": 1}, {"id": 2}, {"id": 3}]
        }
    }
