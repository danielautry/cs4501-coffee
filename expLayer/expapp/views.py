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
from elasticsearch import Elasticsearch
from kafka import KafkaProducer

def index(request):
    return HttpResponse("expLayer")

def viewProduct(request, num):
    req = urllib.request.Request('http://models-api:8000/product/' + str(num) + '/')
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    resp = json.loads(resp_json)
    return JsonResponse(resp)

def viewAllProducts(request):
    req = urllib.request.Request('http://models-api:8000/viewAllProducts/')
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    resp = json.loads(resp_json)
    test_data = {
        "hey" : "heyyo"
    }
    return JsonResponse(resp, safe = False)

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
        return JsonResponse(post_data)
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

@csrf_exempt
def logout(request):
    if request.method == "POST":
        auth = request.POST["Authenticator"]
        post_auth = {
            "Authenticator": auth
        }
        post_encoded = urllib.parse.urlencode(post_auth).encode('utf-8')
        req = urllib.request.Request('http://models-api:8000/customer/logout/', data=post_encoded, method='POST')
        auth_json = urllib.request.urlopen(req).read().decode('utf-8')
        # auth = json.loads(auth_json)
        return JsonResponse({'Success' : 'Auth deleted'}, safe=False)
    return HttpResponse("Delete Auth in EXP failed")

@csrf_exempt
def createProduct(request):
    # dynamically making new ids
    producer = KafkaProducer(bootstrap_servers='kafka:9092')
    if request.method == "POST":
        product = request.POST['product']
        price = request.POST['price']
        auth = request.POST['auth']
        post_data = {
            'product' : product,
            'price' : price,
            'auth' : auth
        }
        expCheck = {'exp' : 'in exp layer'}
        post_encoded = urllib.parse.urlencode(post_data).encode('utf-8')
        req = urllib.request.Request('http://models-api:8000/product/create/', data=post_encoded, method='POST')
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
        resp = json.loads(resp_json)
        producer.send('new-product', json.dumps(resp).encode('utf-8'))
        return JsonResponse(resp, safe=False)
    return JsonResponse({'Error' : 'Exp Layer'})

@csrf_exempt
def search(request):
    # query = ''
    # post_data = {}
    # if request.method == "POST":
    #     query = request.POST['query']
    #     post_data = {
    #         'query': query
    #     }
    #     post_encoded = urllib.parse.urlencode(post_data).encode('utf-8')
    #     req = urllib.request.Request('http://models-api:8000/customer/create/', data=post_encoded, method='POST')
    #     resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    #     resp = json.loads(resp_json)
    #     return JsonResponse(post_data)
    # # return HttpResponse("Not POST in EXP")
    # # if request.method != "POST":
	# es = Elasticsearch(['es'])
    # query = query
	# result = es.search(index = 'listing-indexer', body = {'query': {'query_string':{'query':searchTerm}}})
	# # except Exception as e:
	# # 	return _error_response(request, "Listing failed.")
	# searchResults = []
    return JsonResponse({'Error' : 'Exp Layer'})
