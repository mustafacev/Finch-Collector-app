# Generated by Django 4.2.2 on 2023-06-30 02:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_favoritecarmodel'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cars',
            new_name='CarBrand',
        ),
        migrations.RenameModel(
            old_name='Favoritecarmodel',
            new_name='FavoriteCarsList',
        ),
        migrations.RenameField(
            model_name='carbrand',
            old_name='verified_cars',
            new_name='verified_car',
        ),
        migrations.RenameField(
            model_name='carmodel',
            old_name='accelerationtime',
            new_name='acceleration_time',
        ),
        migrations.RenameField(
            model_name='carmodel',
            old_name='carmodel',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='favoritecarslist',
            old_name='carmodel',
            new_name='car_model',
        ),
        migrations.RenameField(
            model_name='favoritecarslist',
            old_name='model',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='carmodel',
            name='cars',
        ),
        migrations.AddField(
            model_name='carmodel',
            name='car_brand',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='car_model', to='main_app.carbrand'),
            preserve_default=False,
        ),
    ]