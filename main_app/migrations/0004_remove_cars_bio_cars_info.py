# Generated by Django 4.2.2 on 2023-06-24 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_remove_cars_verified_artist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cars',
            name='bio',
        ),
        migrations.AddField(
            model_name='cars',
            name='info',
            field=models.TextField(default='info', max_length=500),
        ),
    ]
