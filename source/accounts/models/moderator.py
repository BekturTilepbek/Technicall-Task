from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Moderator(models.Model):
    user = models.OneToOneField(User, related_name='moderator', on_delete=models.CASCADE, verbose_name='Пользователь')
    field_1 = models.CharField(max_length=100, verbose_name='Поле_1', blank=True)
    field_2 = models.CharField(max_length=100, verbose_name='Поле_2', blank=True)
    field_3 = models.CharField(max_length=100, verbose_name='Поле_3', blank=True)

    def __str__(self):
        return f"Пользователь {self.user.username} - Модератор"

    class Meta:
        verbose_name = 'Модератор'
        verbose_name_plural = 'Модераторы'

