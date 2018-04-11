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

def detail(request):
    template = loader.get_template('coffeeApp/products.html')
    return HttpResponse(template.render(request))

def createCustomer(request):
#trigger create authenticator and get ID

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        cardNumber = request.POST.get('cardNumber')
        password = request.POST.get('password')
        post_data = {'name': name, 'email': email, 'cardNumber': cardNumber, 'password': password}

        post_encoded = urllib.parse.urlencode(post_data).encode('utf-8')

        req = urllib.request.Request('http://exp-api:8000/customer/create/', data=post_encoded, method='POST')
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')

        resp = json.loads(resp_json)
        #put this into the template later

    template = loader.get_template('coffeeApp/createCustomer.html')
    return HttpResponse(template.render(request))
