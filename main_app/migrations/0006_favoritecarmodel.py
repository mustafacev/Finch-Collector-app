# Generated by Django 4.2.2 on 2023-06-28 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_carmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favoritecarmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=150)),
                ('carmodel', models.ManyToManyField(to='main_app.carmodel')),
            ],
        ),
    ]
