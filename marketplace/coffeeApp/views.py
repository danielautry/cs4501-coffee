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

def showCoffee(request):
    print ("About to perform the GET request...")

    req = urllib.request.Request('http://exp-api:8000/coffeeProduct/1/')

    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    resp = json.loads(resp_json)

    return JsonsResponse(resp)
    # return render("It's %s", {'coffeeType': coffee})
