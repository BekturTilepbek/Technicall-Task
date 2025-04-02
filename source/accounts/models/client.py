from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Client(models.Model):
    user = models.OneToOneField(User, related_name='client', on_delete=models.CASCADE, verbose_name='Пользователь')
    field_1 = models.CharField(max_length=100, verbose_name='Поле_1')
    field_2 = models.CharField(max_length=100, verbose_name='Поле_2')
    field_3 = models.CharField(max_length=100, verbose_name='Поле_3')

    def __str__(self):
        return f"Пользователь {self.user.username} - Клиент"

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

