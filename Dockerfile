FROM python:3.13-slim AS builder

WORKDIR /app

RUN pip install poetry

COPY pyproject.toml poetry.lock* ./
COPY src ./src

RUN poetry config virtualenvs.create false \
    && poetry install --only main

FROM python:3.13-slim

WORKDIR /app

COPY --from=builder /usr/local /usr/local
COPY src ./src

EXPOSE 8000

CMD ["uvicorn", "bookstore.main:app", "--host", "0.0.0.0", "--port", "8000"]