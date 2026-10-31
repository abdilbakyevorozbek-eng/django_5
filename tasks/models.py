from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    class Status(models.TextChoices):
        NEW = 'new', 'Новая'
        IN_PROGRESS = 'in_progress', 'В работе'
        COMPLETED = 'completed', 'Завершена'

    title = models.CharField(max_length=150, verbose_name='Название задачи')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks', verbose_name='Автор')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    due_date = models.DateTimeField(blank=True, null=True, verbose_name='Срок выполнения')
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.NEW, verbose_name='Статус')
    priority = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 6)], default=3, verbose_name='Приоритет')

    def __str__(self):
        return self.title
