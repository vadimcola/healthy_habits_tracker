from rest_framework import serializers

from habits.models import Habit
from habits.validators import validate_time_to_complete, validate_period


class HabitSerializer(serializers.ModelSerializer):
    time_to_complete = serializers.IntegerField(validators=[validate_time_to_complete])
    period = serializers.IntegerField(validators=[validate_period])


    class Meta:
        model = Habit
        fields = '__all__'

    def validate(self, data):
        related_habit = data.get('related_habit') # связанная привычка
        reward = data.get('reward') # вознаграждение
        is_pleasant = data.get('is_pleasant') # приятная привычка
        if related_habit and reward:
            raise serializers.ValidationError('Связанная привычка и вознаграждение не могут быть указаны одновременно')
        elif is_pleasant and (reward is not None or related_habit is not None):
            raise serializers.ValidationError(
                "У приятной привычки не может быть вознаграждения или связанной привычки!")
        elif related_habit and not related_habit.is_pleasant:
            raise serializers.ValidationError(
                'Связанная привычка должна быть приятной!')
        return data
