from django.contrib import admin

# Register your models here.
from .models import CarBrand , CarModel , FavoriteCarsList # import the Artist model from models.py
# Register your models here.

admin.site.register(CarBrand) # this line will add the model to the admin panel
admin.site.register(CarModel)
admin.site.register(FavoriteCarsList)