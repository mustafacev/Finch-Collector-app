from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
# import models
from .models import Cars
# Create your views here.


class Home(TemplateView):
    template_name = "home.html"


class About(TemplateView):
    template_name = "about.html"

 # adds artist class for mock database data


# class Car:
#     def __init__(self, name, image,bio):
#         self.name = name
#         self.image = image
#         self.bio = bio


# cars = [
#     Cars("Toyota Corolla", "https://toyota-cms-media.s3.amazonaws.com/wp-content/uploads/2022/10/2023-Corolla-Sedan_001H-1500x900.jpg",
#          "Brand new car."),
#     Cars("Honda Civic",
#          "https://hips.hearstapps.com/hmg-prod/images/2022-honda-civic-hatchback-sport-touring-309-1634066512.jpg?crop=0.617xw:0.520xh;0.298xw,0.477xh&resize=1200:*", " 2023 Honda Civic   ."),
#     Cars("Mazda ", "https://cdn.centraljersey.com/wp-content/uploads/sites/26/2023/01/2022-Mazda-3-Sedan-696x392.jpg",
#          "2022 Mazda 3 Turbo AWD."),
#     Cars("Hyundai",
#          "https://hips.hearstapps.com/hmg-prod/images/2024-hyundai-elantra-n-106-643eb61f5ee7c.jpg?crop=1.00xw:0.567xh;0,0.290xh&resize=1200:*", "2023 Hyundai Elentra."),
#     Cars("Jeep",
#          "https://pictures.dealer.com/g/gengrascdjrfairfieldcllc/0494/cd98dac15382037b7841670a4c0868c8x.jpg", "2023 Wrangler "),
#     Cars("Porsche",
#          "https://hips.hearstapps.com/hmg-prod/images/2023-porsche-911-t-021-dsc04152-1669058415.jpg?crop=0.596xw:0.502xh;0.216xw,0.377xh&resize=1200:*", "2023 Porsche starting at $100k."),
# ]


class CarsList(TemplateView):
    template_name = "cars_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # to get the query parameter we have to acccess it in the request.GET dictionary object
        name = self.request.GET.get("name")
        # If a query exists we will filter by name
        if name != None:
            # .filter is the sql WHERE statement and name__icontains is doing a search for any name that contains the query param
            context["Cars"] = Cars.objects.filter(name__icontains=name)
            # We add a header context that includes the search param
            context["header"] = f"Searching for {name}"
        else:
            context["Cars"] = Cars.objects.all()
            # default header for not searching 
            context["header"] = "Trending Cars"
        return context


class ModelList(TemplateView):
    template_name = "model_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["model"] = models
        return context


# class Model:
#     def __init__(self, title, catalog):
#         self.title = title
#         self.catalog = catalog


# models = [
#     Model("Toyota Tundra", "4x4"),
#     Model("Ford F-150", "4x4")
# ]

class CarCreate(CreateView):
    model = Cars
    fields = ['name', 'img', 'info', 'verified_cars']
    template_name = "car_create.html"
    success_url = "/cars/"

class CarDetail(DetailView):
    model = Cars
    template_name = "car_detail.html"