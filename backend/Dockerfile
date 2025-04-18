FROM python:3.9-slim

WORKDIR /app

# Установка зависимостей
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копирование кода
COPY ./app ./app

# Переменные окружения
ENV PYTHONPATH=/app
ENV PORT=8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]