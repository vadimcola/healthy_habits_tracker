import os
from datetime import datetime
import requests
from celery import shared_task

from habits.models import Habit

TG_ACCESS_TOKEN = os.getenv("TG_ACCESS_TOKEN")


def chat_id(telegram_name):
    request_url = f'https://api.telegram.org/bot{TG_ACCESS_TOKEN}/getUpdates'
    response = requests.get(request_url)
    for i in response.json()['result']:
        if i['message']['from'].get('username') == telegram_name:
            return i['message']['from'].get('id')


@shared_task
def send_tg():
    current_time = datetime.now().time()
    formatted_current_time = f'{current_time.hour:02d}:{current_time.minute:02d}'
    all_habits = Habit.objects.all()
    for habit in all_habits:
        habit_time = f'{habit.time.hour:02d}:{habit.time.minute:02d}'
        if formatted_current_time == habit_time:
            telegram_name = habit.user.telegram_name
            id_chat = chat_id(telegram_name)
            message = (
                f"Напоминание о привычке для пользователя {telegram_name}:\nМесто: {habit.place}\n"
                f"Действие: {habit.action}\nВремя: {habit.time}")
            url = f"https://api.telegram.org/bot{TG_ACCESS_TOKEN}/sendMessage"
            params = {
                "chat_id": id_chat,
                "text": message,
            }
            return requests.get(url, params=params)


