# Используем базовый образ Python
FROM python:3.11

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем зависимости и код приложения
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .
