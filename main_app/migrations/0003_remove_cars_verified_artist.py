# Generated by Django 4.2.2 on 2023-06-24 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_cars_verified_cars'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cars',
            name='verified_artist',
        ),
    ]
