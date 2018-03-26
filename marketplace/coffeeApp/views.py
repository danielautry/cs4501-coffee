from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *
from django.http import JsonResponse
import json
from django.core import serializers
from django.template import loader

from .models import CoffeeProduct
# from .microservices.microapp import models as models


def index(request):
    template = loader.get_template('coffeeApp/index.html')
    return HttpResponse(template.render(request))

def showCoffee(request, num):
    coffee = get_object_or_404(CoffeeProduct, pk=num)
    return HttpResponse("You're looking at coffee product %s." % num)
    # return render("It's %s", {'coffeeProd': coffee})
