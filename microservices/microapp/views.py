from django.shortcuts import render, get_object_or_404
from django.forms.models import model_to_dict
from django.http import HttpResponse
from .models import *
from django.http import JsonResponse
import json
from django.core import serializers

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
        custObj = Customer.objects.all().values('name', 'email', 'cardNumber')
        cust_list = list(custObj)
        if request.method == "POST":
            cust.cardNumber = request.POST.get('newCardNumber')
            cust.save()
        data = {
            "Name" : cust.name,
            "Email" : cust.email,
            "Card Number" : cust.cardNumber
        }
        return JsonResponse(data, safe=False)
    except:
        return JsonResponse({
            "Error": "Customer does not exist"
        })

def createCustomer(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        cardNumber = request.POST.get('cardNumber')
        cust = Customer.objects.create(name = name, email = email, cardNumber = cardNumber)
        cust.save()
        return HttpResponse(cust)
    return HttpResponse("createCustomer Failed")

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
