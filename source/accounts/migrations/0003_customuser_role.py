# Generated by Django 5.1.8 on 2025-04-02 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_client_moderator'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.CharField(default='client', max_length=100, verbose_name='Роль'),
        ),
    ]
