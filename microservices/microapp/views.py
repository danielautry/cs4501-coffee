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
from django.conf import settings

def index(request):
    return JsonResponse({})

def viewProduct(request, num):
    #return JsonResponse({"view ": "product"})
    try:
        prod = get_object_or_404(Product, pk = num)
        if request.method == "POST":
            prod.product = request.POST.get('product')
            prod.price = request.POST.get('price')
            prod.save()
        data = {
            "Product" : prod.product,
            "Price" : prod.price,
            "Seller_Email" : prod.sellerEmail
            }
        return JsonResponse(data, safe=False)
    except:
        return JsonResponse({
            "Error" : "Product does not exist"
        })

def viewAllProducts(request):
    try:
        productDictList = []
        for product in Product.objects.all():
            productDict = model_to_dict(product)
            productDictList.append(productDict)

        dumpJson = json.dumps(productDictList)
        productJson = json.loads(dumpJson)
        return JsonResponse(productJson, safe = False)
    except:
        return JsonResponse({
            "Error": "Product does not exist"
        })

def createProduct(request):
    if request.method == "POST":
        #get user info from auth:
        auth = request.POST['auth']
        existingAuth = Authenticator.objects.get(authenticator = auth)
        if not existingAuth:
            return JsonResponse({'Error' : 'Invalid Auth'}, safe=False)
        customerID = existingAuth.user_id
        customer = Customer.objects.get(id = customerID)
        customerEmail = customer.email
        product = ''
        price = ''
        if 'product' not in (request.POST):
            return JsonResponse({'Error' : 'Invalid Product'})
        else:
            product = request.POST['product']
        if 'price' not in (request.POST):
            return JsonResponse({'Error' : 'Invalid Price'})
        else:
            price = request.POST['price']

        prodInstance = Product.objects.create(product = product, price = price, sellerEmail = customerEmail)
        prodInstance.save()
        jsonProd = {
            "product" : product,
            "price" : price,
            "sellerEmail" : customerEmail
        }
        return JsonResponse(jsonProd)
    return JsonResponse({'Error' : 'createProduct failed'})


def destroyProduct(request, num):
    prod = get_object_or_404(Product, pk = num)
    success = {"Status" : "Delete Successful"}
    error = {"Error" : "Delete Failed"}
    if request.method == "POST":
        prod.delete()
        return JsonResponse(success, safe=False)
    return JsonResponse(error, safe=False)

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
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        cardNumber = request.POST['cardNumber']
        password = request.POST['password']
        cust = Customer.objects.create(name = name, email = email, cardNumber = cardNumber, password = password)
        id = cust.id
        cust.save()
        jsonCust = model_to_dict(cust)
        jsonCust = {
            "name" : name,
            "email" : email,
            "Card Number" : cardNumber,
            "Password" : password
        }
        return JsonResponse(jsonCust)
    return HttpResponse("createCustomer Failed")

def login(request):
    error_data = {'Error' : 'User Invalid'}
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        cust = Customer.objects.get(email = email)
        if Customer.objects.filter(email = email).exists():
            if check_password(password, cust.password):
                # data = {
                #     "Email" : cust.email,
                #     "Password" : cust.password
                #     }
                authString = hmac.new(
                    key = settings.SECRET_KEY.encode('utf-8'),
                    msg = os.urandom(32),
                    digestmod = 'sha256',
                ).hexdigest()
                date_now = datetime.datetime.now()
                auth = Authenticator.objects.create(user_id = cust.id, authenticator = authString, date_created = date_now)
                auth.save()
                authenticator = {
                    'ID' : cust.id,
                    'Authenticator' : authString,
                    'Date' : date_now,
                    'ok' : True
                }
                return JsonResponse(authenticator, safe=False)
    return JsonResponse(error_data)

def logout(request):
    error_data = {'Error' : 'User Invalid'}
    delete_successful = False
    if request.method == "POST":
        auth = request.POST['Authenticator']
        existingAuth = Authenticator.objects.get(authenticator = auth)
        if not existingAuth:
            return JsonResponse({'Error' : 'You are already logged out'}, safe=False)
        existingAuth.delete()
        return JsonResponse({"Deleted" : True})
    return JsonResponse(error_data)

def destroyCustomer(request, num):
    cust = get_object_or_404(Customer, pk = num)
    success = {"Status" : "Delete Successful"}
    error = {"Error" : "Delete Failed"}
    if request.method == "POST":
        cust.delete()
        return JsonResponse(success, safe=False)
    return JsonResponse(error, safe=False)

# def viewSale(request, num):
#     try:
#         purchase = Sale.objects.get(pk = num)
#         if request.method == "POST":
#             purchase.amount = request.POST.get('newAmount')
#             purchase.save()
#         data1 = serializers.serialize('json', [purchase,])
#         struct = json.loads(data1)
#         data1 = json.dumps(struct[0])
#         return HttpResponse(data1)
#     except:
#         return JsonResponse({
#             "Error": "Sale does not exist"
#         })


# def createSale(request):
#     if request.method == "POST":
#         amount = request.POST.get('amount')
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         product = request.POST.get('product')
#
#         #GUNNA BE SOME ISSUES HERE - UNIQUE PRODUCTS
#         cust = Customer.objects.get(name = name, email = email)
#         product = Product.objects.get(product = product)
#
#         purchase = Sale.objects.create(salesman = salesman, amount = amount, customer = cust, product = product)
#         purchase.save()
#         return HttpResponse(purchase)
#     return HttpResponse("createSale Failed")

# def destroySale(request, num):
#     purchase = get_object_or_404(Sale, pk = num)
#     if request.method == "POST":
#         purchase.delete()
#         return HttpResponse("Delete Successful")
#     return HttpResponse("destroySale Failed")


#start jeremy Tuesday edits
