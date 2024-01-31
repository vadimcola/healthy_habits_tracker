from rest_framework import serializers


def validate_time_to_complete(value):
    if value > 120:
        raise serializers.ValidationError('Время выполнения должно быть не больше 120 секунд!')


def validate_period(value):
    if value > 7:
        raise serializers.ValidationError('Привычка не может быть выполнена реже, чем 1 раз в 7 дней!')
