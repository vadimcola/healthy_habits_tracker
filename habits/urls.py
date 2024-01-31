from django.urls import path

from habits.apps import HabitsConfig
from habits.views import HabitList, HabitDetail, HabitCreate, HabitUpdate, HabitDelete, HabitPublicList

app_name = HabitsConfig.name

urlpatterns = [
    path('habit/', HabitList.as_view(), name='list'),
    path('habit/<int:pk>/', HabitDetail.as_view(), name='detail'),
    path('habit/create/', HabitCreate.as_view(), name='create'),
    path('habit/<int:pk>/update/', HabitUpdate.as_view(), name='update'),
    path('habit/<int:pk>/delete/', HabitDelete.as_view(), name='delete'),
    path('habit/public/', HabitPublicList.as_view(), name='public_list'),

]
