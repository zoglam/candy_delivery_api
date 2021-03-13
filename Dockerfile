# ------------ BUILDER ------------
FROM python:3.7-alpine3.12 as builder

RUN apk --update add gcc mariadb-dev mariadb-client musl-dev

COPY ./requirements.txt /mnt/requirements.txt

RUN python3 -m venv /app/venv
RUN app/venv/bin/pip install -Ur /mnt/requirements.txt
RUN app/venv/bin/pip check

# ------------ MAIN ------------
FROM python:3.7-alpine3.12

COPY ./app /app
COPY --from=builder /app /app

WORKDIR /app

EXPOSE 8000

CMD ["/app/venv/bin/uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
