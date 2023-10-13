from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse

from habits.models import Habit
from users.models import User


class HabitTest(APITestCase):
    def setUp(self):
        self.user_data = {'email': 'test@test.com', 'password': '12345'}
        self.user = User.objects.create(**self.user_data)
        self.client.force_authenticate(user=self.user)

        self.habit = Habit.objects.create(
            time_to_complete=10,
            place='Test',
            time='00:00',
            user=self.user,
            action='Test',
            is_pleasant=False,
            period=1,
            reward="test",
            is_public=False,
            related_habit=None
        )

    def test_habit_create(self):
        """Тест создания привычки"""
        data_habit = {
            "time_to_complete": 10,
            "period": 1,
            "place": "Test",
            "time": "00:00",
            "action": "Test",
            "is_pleasant": False,
            "reward": "test",
            "is_public": False,
            "user": self.user.id,
            "related_habit": None
        }
        response = self.client.post(reverse('habits:create'), data_habit, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_habit_detail(self):
        """Тест на просмотр привычки"""
        response = self.client.get(reverse('habits:detail', args=[self.habit.pk]), )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.json(), {
            'id': 1,
            "time_to_complete": 10,
            "period": 1,
            "place": "Test",
            "time": "00:00:00",
            "action": "Test",
            "is_pleasant": False,
            "reward": "test",
            "is_public": False,
            "user": self.user.id,
            "related_habit": None})

    def test_habit_delete(self):
        """Тест на удаление привычки"""
        response = self.client.delete(reverse('habits:delete', args=[self.habit.pk]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_habit_update(self):
        """Тест на обновление привычки """
        data = {
            "place": "Тест измененный",
            "reward": "Тест измененный"
        }

        response = self.client.patch(reverse('habits:update', args=[self.habit.pk]), data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.json(), {
            'id': 1,
            "time_to_complete": 10,
            "period": 1,
            "place": "Тест измененный",
            "time": "00:00:00",
            "action": "Test",
            "is_pleasant": False,
            "reward": "Тест измененный",
            "is_public": False,
            "user": self.user.id,
            "related_habit": None})

    def test_habits_list(self):
        """Тест на просмотр списка привычек"""
        response = self.client.get(reverse('habits:list'), )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.json(), {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    'id': 1,
                    "time_to_complete": 10,
                    "period": 1,
                    "place": "Test",
                    "time": "00:00:00",
                    "action": "Test",
                    "is_pleasant": False,
                    "reward": "test",
                    "is_public": False,
                    "user": self.user.id,
                    "related_habit": None}], })
