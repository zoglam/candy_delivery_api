# candy_delivery_api

[![Flake8](https://github.com/zoglam/candy_delivery_api/actions/workflows/flake8.yml/badge.svg?branch=master)](https://github.com/zoglam/candy_delivery_api/actions/workflows/flake8.yml)
[![Pytest](https://github.com/zoglam/candy_delivery_api/actions/workflows/pytest.yml/badge.svg?branch=master)](https://github.com/zoglam/candy_delivery_api/actions/workflows/pytest.yml)

## Cmd

Prepare
```sh
python3 -m pip install -r requirements.txt
```

Run
```sh
uvicorn app.main:app --reload
```

## Docker-compose

Run
```sh
docker-compose up -d --build
```

## Pytest

Prepare
```sh
docker run -d -p 3306:3306 -e "MYSQL_ROOT_PASSWORD=secret" -e "MYSQL_DATABASE=test" mariadb:10.5
```

Run
```sh
pytest
```
