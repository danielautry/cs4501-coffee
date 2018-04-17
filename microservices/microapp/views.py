from django.shortcuts import render, get_object_or_404
from django.forms.models import model_to_dict
from django.http import HttpResponse
from .models import *
from django.http import JsonResponse
import json
from django.core import serializers
import os
import hmac
import datetime
import pdb
from django.contrib.auth.hashers import make_password, check_password
# import settings

def index(request):
    return JsonResponse({})

def viewCoffeeProduct(request, num):
    try:
        coffeeProd = get_object_or_404(CoffeeProduct, pk = num)
        if request.method == "POST":
            coffeeProd.price = request.POST.get('newPrice')
            coffeeProd.save()
        data = {
            "Coffee_Product" : coffeeProd.coffeeType,
            "Price" : coffeeProd.price
            }
        return JsonResponse(data, safe=False)
    except:
        return JsonResponse({
            "Error": "Coffee Product does not exist"
        })


def createCoffeeProduct(request):
    if request.method == "POST":
        coffeeType = request.POST.get('coffeeType')
        price = request.POST.get('price')
        coffeeProd = CoffeeProduct.objects.create(price = price, coffeeType = coffeeType)
        coffeeProd.save()
        # return JsonResponse(model_to_dict(coffeeProd))
        return HttpResponse("Success!")
    return HttpResponse("createCoffeeProduct Failed")

def destroyCoffeeProduct(request, num):
    coffeeProd = get_object_or_404(CoffeeProduct, pk = num)
    if request.method == "POST":
        coffeeProd.delete()
        return HttpResponse("Delete Successful")
    return HttpResponse("DeleteCoffeeProduct Failed")

def viewCustomer(request, num):
    try:
        cust = get_object_or_404(Customer, pk = num)
        custObj = Customer.objects.all().values('name', 'email', 'cardNumber', 'password')
        cust_list = list(custObj)
        if request.method == "POST":
            cust.cardNumber = request.POST.get('newCardNumber')
            cust.save()
        data = {
            "Name" : cust.name,
            "Email" : cust.email,
            "Card_Number" : cust.cardNumber,
            "Password" : cust.password
        }
        return JsonResponse(data, safe=False)
    except:
        return JsonResponse({
            "Error": "Customer does not exist"
        })

def createCustomer(request):

    #CREATE AUTHENTICATOR HERE
    # authString = hmac.new(
    #     key = settings.SECRET_KEY.encode('utf-8'),
    #     msg = os.urandom(32),
    #     digestmod = 'sha256',
    # ).hexdigest()

    if request.method == "POST":
        #first create customer to DB
        name = request.POST['name']
        email = request.POST['email']
        cardNumber = request.POST['cardNumber']
        password = request.POST['password']
        cust = Customer.objects.create(name = name, email = email, cardNumber = cardNumber, password = password)
        id = cust.id #THIS LINE IS WRONG BUT ALMOST RIGHT
        cust.save()
        jsonCust = model_to_dict(cust)
        jsonCust = {
            "name" : name,
            "email" : email,
            "Card Number" : cardNumber,
            "Password" : password
        }

        # Authenticator next
        # date_now = datetime.datetime.now()
        # auth = Authenticator.objects.create(user_id = id, authenticator = authString, date_created = date_now)
        # auth.save()

        return JsonResponse(jsonCust)
    return HttpResponse("createCustomer Failed")

def findCustomer(request):
    error_data = {"Error" : "Invalid User"}
    if request.method == "POST":
        #lookup customer by email and password
        email = request.POST['email']
        password = request.POST['password']
        cust = Customer.objects.get(email = email, password = password)
        if Customer.objects.filter(email = email, password = password).exists():
            # if check_password(password, cust.password):
            data = {
                "Email" : cust.email,
                "Password" : cust.password
                }
            return JsonResponse(data, safe=False)
    return JsonResponse(error_data)

def destroyCustomer(request, num):
    cust = get_object_or_404(Customer, pk = num)
    if request.method == "POST":
        cust.delete()
        return HttpResponse("Delete Successful")
    return HttpResponse("destroyCustomer Failed")

def viewSale(request, num):
    try:
        purchase = Sale.objects.get(pk = num)
        if request.method == "POST":
            purchase.amount = request.POST.get('newAmount')
            purchase.save()
        data1 = serializers.serialize('json', [purchase,])
        struct = json.loads(data1)
        data1 = json.dumps(struct[0])
        return HttpResponse(data1)
    except:
        return JsonResponse({
            "Error": "Sale does not exist"
        })


def createSale(request):
    if request.method == "POST":
        salesman = request.POST.get('salesman')
        amount = request.POST.get('amount')
        name = request.POST.get('name')
        email = request.POST.get('email')
        coffeeType = request.POST.get('coffeeType')

        cust = Customer.objects.get(name = name, email = email)
        coffee = CoffeeProduct.objects.get(coffeeType = coffeeType)

        purchase = Sale.objects.create(salesman = salesman, amount = amount, customer = cust, coffeeProduct = coffee)
        purchase.save()
        return HttpResponse(purchase)
    return HttpResponse("createSale Failed")

def destroySale(request, num):
    purchase = get_object_or_404(Sale, pk = num)
    if request.method == "POST":
        purchase.delete()
        return HttpResponse("Delete Successful")
    return HttpResponse("destroySale Failed")
