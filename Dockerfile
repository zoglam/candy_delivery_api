# ------------ BUILDER ------------
FROM python:3.7-alpine3.12 as builder

RUN apk --update add gcc mariadb-dev mariadb-client musl-dev

COPY ./app /app

RUN python3 -m venv /app/venv

COPY ./requirements.txt /mnt/requirements.txt

RUN app/venv/bin/pip install -Ur /mnt/requirements.txt

RUN app/venv/bin/pip check

# ------------ MAIN ------------
FROM alpine:3.12

RUN apk update && apk upgrade

COPY --from=builder /app /app

CMD ["/app/venv/bin/uvicorn", "main:app", "--app-dir", "app"]
