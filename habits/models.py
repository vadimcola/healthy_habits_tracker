from django.db import models

from config import settings
from users.models import NULLABLE


class Habit(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE,
                             verbose_name='Пользователь')  # создатель привычки
    place = models.CharField(max_length=255, verbose_name='Место')  # место, в котором необходимо выполнять привычку
    time = models.TimeField(verbose_name='Время')  # время, когда необходимо выполнять привычку
    action = models.CharField(max_length=255,
                              verbose_name='Действие')  # действие, которое является привычкой
    is_pleasant = models.BooleanField(default=False, verbose_name='Признак приятной привычки')  # признак приятной привычки
    related_habit = models.ForeignKey('self', on_delete=models.SET_NULL, **NULLABLE,
                                      verbose_name='Связанная привычка')  # связанная привычка
    period = models.PositiveIntegerField(default=1, verbose_name='Периодичность (в днях)')  # периодичность выполнения
    # привычки для напоминания в днях
    reward = models.CharField(max_length=255, verbose_name='Вознаграждение', **NULLABLE)  # чем пользователь должен
    # себя вознаградить после выполнения
    time_to_complete = models.PositiveIntegerField(verbose_name='Время на выполнение')  # время, которое
    # предположительно потратит пользователь на выполнение привычки
    is_public = models.BooleanField(default=False, verbose_name='Признак публичности')  # привычки можно публиковать в
    # общий доступ, чтобы другие пользователи могли брать в пример чужие привычки

    def __str__(self):
        return f'{self.action}'

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
