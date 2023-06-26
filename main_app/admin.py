from django.contrib import admin

# Register your models here.
from .models import Cars , Carmodel# import the Artist model from models.py
# Register your models here.

admin.site.register(Cars) # this line will add the model to the admin panel
admin.site.register(Carmodel)