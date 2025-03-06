from django.db import models


class Task(models.Model):
    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    title = models.CharField(
        max_length=255,
        verbose_name='Название задачи'
    )
    description = models.TextField(
        verbose_name='Описание задачи'
    )
    status  = models.BooleanField(
        default=False,
        verbose_name='Статус задачи',
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Последное обнавление'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создание'
    )

    def __str__(self):
        return self.title