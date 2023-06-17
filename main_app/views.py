from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
# Create your views here.

class Home(View):
      def get(self, request):
        # Here we are returning a generic response
        # This is similar to response.send() in express
        return HttpResponse("Cars Home page")