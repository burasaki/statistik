FROM python:3.12-slim-bookworm

COPY --from=ghcr.io/astral-sh/uv:0.9.7 /uv /uvx /bin/

COPY . /app

WORKDIR /app

RUN uv sync --locked

CMD [ "uv", "run", "main.py" ]