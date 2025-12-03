FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    POETRY_VERSION=1.8.3 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_NO_INTERACTION=1

WORKDIR /app

# System build deps (kept minimal; extend as needed)
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN pip install "poetry==${POETRY_VERSION}"

# Copy dependency metadata first (better layer caching)
COPY pyproject.toml poetry.lock ./ 

# Copy local path dependency for openapi-client
COPY noaa_client ./noaa_client

# Copy application code
COPY app ./app

# Install dependencies (no dev, no project package)
RUN poetry install --no-root --only main

EXPOSE 8000

CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]


