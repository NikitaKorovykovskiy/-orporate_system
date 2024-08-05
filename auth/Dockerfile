# Используем официальный образ Python
FROM python:3.11-slim

# Устанавливаем зависимости системы
RUN apt-get update && \
    apt-get install -y \
    curl \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Добавляем Poetry в PATH
ENV PATH="/root/.local/bin:$PATH"

# Создаем рабочую директорию
WORKDIR /app

# Копируем файлы конфигурации Poetry
COPY pyproject.toml poetry.lock* /app/

# Устанавливаем зависимости с Poetry
RUN poetry install --no-dev

# Копируем оставшиеся файлы проекта
COPY . /app

# Выполняем миграции и запускаем приложение
ENTRYPOINT ["sh", "-c", "poetry run alembic upgrade head && poetry run uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload"]
