# Generated by Django 4.2.2 on 2023-06-24 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cars',
            name='verified_cars',
            field=models.BooleanField(default=False),
        ),
    ]