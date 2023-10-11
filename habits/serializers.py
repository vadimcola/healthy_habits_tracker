from rest_framework import serializers

from habits.models import Habit
from habits.validators import validate_time_to_complete, validate_period, validate_related_habit


class HabitSerializer(serializers.ModelSerializer):
    time_to_complete = serializers.IntegerField(validators=[validate_time_to_complete])
    period = serializers.IntegerField(validators=[validate_period])
    related_habit = serializers.PrimaryKeyRelatedField(queryset=Habit.objects.all(), required=False,
                                                       validators=[validate_related_habit])

    class Meta:
        model = Habit
        fields = '__all__'
