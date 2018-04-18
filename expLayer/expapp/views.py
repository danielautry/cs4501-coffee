from django.shortcuts import render, get_object_or_404
from django.forms.models import model_to_dict
from django.http import HttpResponse
from .models import *
from django.http import JsonResponse
import json
from django.core import serializers
import urllib.request
import urllib.parse
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return HttpResponse("expLayer")

def viewCoffeeProduct(request, num):
    req = urllib.request.Request('http://models-api:8000/coffeeProduct/' + str(num) + '/')
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    resp = json.loads(resp_json)
    return JsonResponse(resp)

def viewCustomer(request, num):
    req = urllib.request.Request('http://models-api:8000/customer/' + str(num) + '/')
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    resp = json.loads(resp_json)
    return JsonResponse(resp)

@csrf_exempt
def createCustomer(request):
    name = ''
    email = ''
    cardNumber = ''
    password = ''
    post_data = {}
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        cardNumber = request.POST['cardNumber']
        password = request.POST['password']
        post_data = {
            'name': name,
            'email': email,
            'cardNumber': cardNumber,
            'password': password
        }
        post_encoded = urllib.parse.urlencode(post_data).encode('utf-8')
        req = urllib.request.Request('http://models-api:8000/customer/create/', data=post_encoded, method='POST')
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
        resp = json.loads(resp_json)
        return JsonResponse(resp)
    return HttpResponse("Not POST in EXP")

@csrf_exempt
def login(request):
    email = ''
    password = ''
    post_data = {}
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        post_data = {
            'email': email,
            'password': password
        }
        post_encoded = urllib.parse.urlencode(post_data).encode('utf-8')
        req = urllib.request.Request('http://models-api:8000/customer/login/', data=post_encoded, method='POST')
        auth_json = urllib.request.urlopen(req).read().decode('utf-8')
        auth = json.loads(auth_json)
        return JsonResponse(auth, safe=False)
    return HttpResponse("Not POST in EXP")
