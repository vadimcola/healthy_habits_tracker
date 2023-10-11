
from rest_framework import generics

from habits.models import Habit
from habits.paginators import HabitPaginator
from habits.serializers import HabitSerializer


class HabitList(generics.ListAPIView):
    """Просмотр списка привычек"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = HabitPaginator


class HabitDetail(generics.RetrieveAPIView):
    """Посмотр детальной информации привычки"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class HabitCreate(generics.CreateAPIView):
    """Создание привычки"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

    def perform_create(self, serializer):
        """При создании привычки его владелец, авторизованный пользователь """
        new_habit = serializer.save(user=self.request.user)
        new_habit.user = self.request.user
        new_habit.save()


class HabitUpdate(generics.UpdateAPIView):
    """Обновоение привычки"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class HabitDelete(generics.DestroyAPIView):
    """Удаление привычки"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
