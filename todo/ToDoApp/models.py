from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Task(models.Model):
    """
    model for Task entity
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    description = models.TextField(
        null=True, blank=True, verbose_name="Описание")
    isComplete = models.BooleanField(default=False, verbose_name="Готово")
    create = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания")
    deadline = models.DateTimeField(
        null=True, blank=True, verbose_name="Крайний срок")
    group = models.ForeignKey(
        'Group', null=True, on_delete=models.SET_NULL, verbose_name="Группа", blank=True)

    class Meta:
        ordering = ['isComplete']
        verbose_name_plural = 'Задачи'
        verbose_name = 'Задача'

    def __str__(self):
        return self.title


class Group(models.Model):
    """
    task group model
    """
    name = models.CharField(
        max_length=30, db_index=True, verbose_name="Группа")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Группы'
        verbose_name = 'Группа'

    def __str__(self):
        return self.name
