from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
# Create your views here.

class Home(TemplateView):
    template_name = "home.html"
class About(TemplateView):
    template_name = "about.html"

 #adds artist class for mock database data
class Cars:
    def __init__(self, name, image, info):
        self.name = name
        self.image = image
        self.info = info


cars = [
  Cars("Toyota Corolla", "https://toyota-cms-media.s3.amazonaws.com/wp-content/uploads/2022/10/2023-Corolla-Sedan_001H-1500x900.jpg",
          "Brand new car."),
  Cars("Honda Civic",
          "https://hips.hearstapps.com/hmg-prod/images/2022-honda-civic-hatchback-sport-touring-309-1634066512.jpg?crop=0.617xw:0.520xh;0.298xw,0.477xh&resize=1200:*", " 2023 Honda Civic   ."),
  Cars("Mazda ", "https://cdn.centraljersey.com/wp-content/uploads/sites/26/2023/01/2022-Mazda-3-Sedan-696x392.jpg",
          "2022 Mazda 3 Turbo AWD."),
  Cars("Hyundai",
          "https://hips.hearstapps.com/hmg-prod/images/2024-hyundai-elantra-n-106-643eb61f5ee7c.jpg?crop=1.00xw:0.567xh;0,0.290xh&resize=1200:*", "2023 Hyundai Elentra."),
  Cars("Jeep",
          "https://pictures.dealer.com/g/gengrascdjrfairfieldcllc/0494/cd98dac15382037b7841670a4c0868c8x.jpg", "2023 Wrangler "),
  Cars("Porsche",
          "https://hips.hearstapps.com/hmg-prod/images/2023-porsche-911-t-021-dsc04152-1669058415.jpg?crop=0.596xw:0.502xh;0.216xw,0.377xh&resize=1200:*", "2023 Porsche starting at $100k."),
]

class CarsList(TemplateView):
    template_name = "cars_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Cars"] = cars # this is where we add the key into our context object for the view to use
        return context