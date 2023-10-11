from rest_framework.exceptions import ValidationError
from rest_framework import serializers


def validate_time_to_complete(value):
    if value > 120:
        raise ValidationError('Время выполнения должно быть не больше 120 секунд!')


def validate_period(value):
    if value > 7:
        raise ValidationError('Привычка не может быть выполнена реже, чем 1 раз в 7 дней!')


def validate_related_habit(value):
    if value and not value.is_pleasant:
        raise serializers.ValidationError('Связанная привычка должна быть приятной!')
