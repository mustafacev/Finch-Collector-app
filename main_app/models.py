from django.db import models

# Create your models here.


class CarBrand(models.Model):

    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    info = models.TextField(max_length=500, default='info')
    verified_car = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class CarModel(models.Model):

    name = models.CharField(max_length=150)
    acceleration_time = models.IntegerField(default=0)
    car_brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE, related_name="car_model")

    def __str__(self):
        return self.name

class FavoriteCarsList(models.Model):

    name = models.CharField(max_length=150)
    # this is going to create the many to many relationship and join table
    car_model = models.ManyToManyField(CarModel)

    def __str__(self):
        return self.name
