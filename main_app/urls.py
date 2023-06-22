from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
 path('', views.Home.as_view(), name='home'),
 path('about/', views.About.as_view(), name='about'),
 path('cars/', views.CarsList.as_view(), name="cars_list"),
 path('songs/', views.ModelList.as_view(), name="model_list"),
]