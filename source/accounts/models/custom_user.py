from django.contrib.auth.models import AbstractUser
from django.db import models

ROLES = [('client', 'Клиент'), ('moderator', 'Модератор')]
CLIENT = ROLES[0][0]
MODERATOR = ROLES[1][0]


class CustomUser(AbstractUser):
    role = models.CharField(max_length=100, default=CLIENT, verbose_name='Роль')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
