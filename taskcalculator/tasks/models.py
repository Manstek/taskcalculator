from django.db import models

class TaskInput(models.Model):
    raw_data = models.TextField("Входные данные", help_text="Введите данные в табличном формате через пробел.")
    td = models.IntegerField("Диррективное время")
    created_at = models.DateTimeField(auto_now_add=True)
