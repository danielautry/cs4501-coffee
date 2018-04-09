from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *
from django.http import JsonResponse
import json
from django.core import serializers
from django.template import loader
import urllib.request
import urllib.parse

from .models import CoffeeProduct
# from .microservices.microapp import models as models


def index(request):
    template = loader.get_template('coffeeApp/index.html')
    return HttpResponse(template.render(request))

def showCoffee(request, num):

    #coffee = get_object_or_404(CoffeeProduct, pk=num)
    #print ("About to perform the HTML GET request...")
    url = 'http://exp-api:8000/coffeeProduct/' + str(num) + '/'
    req = urllib.request.Request('http://exp-api:8000/coffeeProduct/' + str(num) + '/')

    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    resp = json.loads(resp_json)

    return render(request, 'coffeeApp/itemDetail.html', resp)




def showAllCoffee(request):

    #coffee = get_object_or_404(CoffeeProduct, pk=num)
    #print ("About to perform the HTML GET request...")

    req = urllib.request.Request('http://exp-api:8000/coffeeProduct/')

    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    resp = json.loads(resp_json)
    return render(request, 'coffeeApp/itemDetail.html', resp)
