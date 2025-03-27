FROM python:3.11-alpine3.18
LABEL authors="pitrlabs"

WORKDIR /app

RUN apk add --no-cache --no-check-certificate\
    mariadb-dev \
    gcc \
    musl-dev \
    libffi-dev \
    openssl-dev \
    pkgconf \
    pkgconfig

RUN apk add --no-cache curl unzip --no-check-certificate

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

RUN apk add --no-cache curl unzip --no-check-certificate

ENV PATH="/root/.local/bin:$PATH"

COPY . /app/

RUN uv sync

