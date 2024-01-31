<h1 align="center">Healthy Habits Tracker</h1>
Данное приложение предназначено для отслеживания ваших здоровых привычек и поможет вам поддерживать их.

## Стек технологий:
- python
- django
- djangorestframework
- djangorestframework-simplejwt
- django-filters
- psycopg2-binary
- coverage
- drf-yasg
- django-cors-headers
- celery
- redis
- django-celery-beat
- docker
- docker-compose

## Установка

**Инструкция по работе с Dockerfile и docker-compose**

Для запуска проекта 
Собираем образ с помощью команды:  ***docker-compose build***<br>
Запустите контейнеры с помощью команды:  ***docker-compose up***<br>
Миграции применяются автоматически<br>
После запуска проекта в терминале запускаем команду для создания суперпользователя:<br> 
***docker-compose exec app python manage.py add_su***

Суперпользователь:
email: test@test.ru
password: 12345






