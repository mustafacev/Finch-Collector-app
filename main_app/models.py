from django.db import models

# Create your models here.


class Cars(models.Model):

    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    info = models.TextField(max_length=500, default='info')
    verified_cars = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Carmodel(models.Model):

    carmodel = models.CharField(max_length=150)
    accelerationtime = models.IntegerField(default=0)
    cars = models.ForeignKey(Cars, on_delete=models.CASCADE, related_name="carmodel")

    def __str__(self):
        return self.carmodel
