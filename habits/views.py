from rest_framework import generics

from habits.models import Habit
from habits.paginators import HabitPaginator
from habits.serializers import HabitSerializer


class MixinQueryset:

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user.pk)
        return queryset


class HabitList(MixinQueryset, generics.ListAPIView):
    """Просмотр списка привычек"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = HabitPaginator


class HabitDetail(MixinQueryset, generics.RetrieveAPIView):
    """Посмотр детальной информации привычки"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class HabitCreate(generics.CreateAPIView):
    """Создание привычки"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

    def perform_create(self, serializer):
        """При создании привычки его владелец, авторизованный пользователь"""
        new_habit = serializer.save(user=self.request.user)
        new_habit.user = self.request.user
        new_habit.save()


class HabitUpdate(MixinQueryset, generics.UpdateAPIView):
    """Обновоение привычки"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class HabitDelete(MixinQueryset, generics.DestroyAPIView):
    """Удаление привычки"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class HabitPublicList(generics.ListAPIView):
    """Просмотр списка публичных привычек"""
    queryset = Habit.objects.filter(is_public=True)
    serializer_class = HabitSerializer
