from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *
from django.http import JsonResponse
import json
from django.core import serializers
from django.template import loader
import urllib.request
import urllib.parse
from .forms import NameForm
from .forms import LoginForm
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
import pdb
from django.contrib.auth.hashers import make_password, check_password

def index(request):
    template = loader.get_template('coffeeApp/index.html')
    return HttpResponse(template.render(request))

def showCoffee(request, num):
    url = 'http://exp-api:8000/coffeeProduct/' + str(num) + '/'
    req = urllib.request.Request('http://exp-api:8000/coffeeProduct/' + str(num) + '/')
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    resp = json.loads(resp_json)
    return render(request, 'coffeeApp/itemDetail.html', resp)

def detail(request):
    template = loader.get_template('coffeeApp/products.html')
    return HttpResponse(template.render(request))

def viewFormResults(request):
    template = loader.get_template('coffeeApp/viewFormResults.html')
    return HttpResponse(template.render(request))

@csrf_exempt
def createAccount(request):
    name = ''
    email = ''
    cardNumber = ''
    password = ''
    post_data = {}
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            cardNumber = form.cleaned_data['cardNumber']
            password = form.cleaned_data['password']
            # hashedPassword = make_password(password, salt=None, hasher='default')
            post_data = {
                'name': name,
                'email': email,
                'cardNumber': cardNumber,
                'password': password
            }
            post_encoded = urllib.parse.urlencode(post_data).encode('utf-8')
            req = urllib.request.Request('http://exp-api:8000/customer/create/', data=post_encoded, method='POST')
            resp_json = urllib.request.urlopen(req).read().decode('utf-8')
            resp = json.loads(resp_json)
            return JsonResponse(resp, safe=False)
    else:
        form = NameForm()
    return render(request, 'coffeeApp/account.html', post_data)

@csrf_exempt
def login(request):
    email = ''
    password = ''
    post_data = {}
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            # hashedPassword = make_password(password, salt=None, hasher='default')
            post_data = {
                'email': email,
                'password': password
            }
            post_encoded = urllib.parse.urlencode(post_data).encode('utf-8')
            req = urllib.request.Request('http://exp-api:8000/customer/login/', data=post_encoded, method='POST')
            resp_json = urllib.request.urlopen(req).read().decode('utf-8')
            resp = json.loads(resp_json)
            return JsonResponse(resp, safe=False)
    else:
        form = LoginForm()
    return render(request, 'coffeeApp/loggedin.html', post_data)
