from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
 path('', views.Home.as_view(), name='home'),
 path('about/', views.About.as_view(), name='about'),
 path('cars/', views.CarsList.as_view(), name="cars_list"),
#  path('cars/', views.ModelList.as_view(), name="model_list"),
 path('cars/new/', views.CarCreate.as_view(), name="car_create"),
 path('cars/<int:pk>/', views.CarDetail.as_view(), name="car_detail"),
 path('cars/<int:pk>/update/',views.CarUpdate.as_view(), name="car_update"),
 path('cars/<int:pk>/delete',views.CarDelete.as_view(), name="car_delete"),
 path('cars/<int:pk>/carmodel/new/', views.CarModelCreate.as_view(), name="car_model_create"),
 path('favoritecarmodel/<int:pk>/carmodel/<int:carmodel_pk>/', views.FavoriteCarsListCarModelAssoc.as_view(), name="favorite_cars_list_car_model_assoc"),
]