# Generated by Django 4.2.2 on 2024-09-08 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='users',
            options={'permissions': [('views_list_users', 'Может просматривать список пользователей сервиса'), ('block_users_service', 'Может блокировать пользователей сервиса')], 'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
    ]
