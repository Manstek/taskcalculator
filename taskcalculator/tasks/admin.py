from django.contrib import admin
from .models import TaskInput

@admin.register(TaskInput)
class TaskInputAdmin(admin.ModelAdmin):
    list_display = ('id', 'raw_data', 'td', 'created_at')  # Добавьте 'id'