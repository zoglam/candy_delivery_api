# candy_delivery_api

[![Flake8](https://github.com/zoglam/candy_delivery_api/actions/workflows/flake8.yml/badge.svg?branch=master)](https://github.com/zoglam/candy_delivery_api/actions/workflows/flake8.yml)
[![Pytest](https://github.com/zoglam/candy_delivery_api/actions/workflows/pytest.yml/badge.svg?branch=master)](https://github.com/zoglam/candy_delivery_api/actions/workflows/pytest.yml)

Create .env file in root directory and add following values:

```sh
DATABASE_URL=mysql://username:password@serverdomain/database
```

```sh
python3 -m pip install -r requirements.txt
```

```sh
uvicorn app.main:app --reload
```

```sh
docker-compose up -d --build
```
