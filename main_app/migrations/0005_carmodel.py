# Generated by Django 4.2.2 on 2023-06-25 23:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_remove_cars_bio_cars_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carmodel', models.CharField(max_length=150)),
                ('accelerationtime', models.IntegerField(default=0)),
                ('cars', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carmodel', to='main_app.cars')),
            ],
        ),
    ]
