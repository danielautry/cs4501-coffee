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
    # if request.method == "POST":
    name = request.GET['name']
    email = request.GET['email']
    cardNumber = request.GET['cardNumber']
    password = request.GET['password']
    post_data = {'name': name, 'email': email, 'cardNumber': cardNumber, 'password': password}
    post_encoded = urllib.parse.urlencode(post_data).encode('utf-8')
    req = urllib.request.Request('http://models-api:8000/customer/create/', data=post_encoded, method='POST')
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    resp = json.loads(resp_json)
    return render(request, post_data)
    # return HttpResponse("Not POST in EXP")

#

# def testPost(request):
#
#     # make a POST request.
#     # we urlencode the dictionary of values we're passing up and then make the POST request
#     # again, no error handling
#
#     print ("About to perform the POST request...")
#
#     post_data = {'coffeeType': 'Java java', 'price': '3000', 'userId': 5}
#
#     post_encoded = urllib.parse.urlencode(post_data).encode('utf-8')
#
#     req = urllib.request.Request('http://models-api:8000/coffeeProduct/create/', data=post_encoded, method='POST')
#     resp_json = urllib.request.urlopen(req).read().decode('utf-8')
#
#     resp = json.loads(resp_json)
#     return JsonResponse(resp)
