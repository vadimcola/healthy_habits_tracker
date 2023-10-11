from django.contrib import admin

from habits.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'place', 'action')
