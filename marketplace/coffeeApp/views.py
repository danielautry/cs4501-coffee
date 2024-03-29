from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import JsonResponse
import json
from django.core import serializers
from django.template import loader
import urllib.request
import urllib.parse
from .forms import NameForm
from .forms import LoginForm
from .forms import SearchForm
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
import pdb
from django.contrib.auth.hashers import make_password, check_password

def index(request):
    auth = request.COOKIES.get('auth')
    if auth:
        template = loader.get_template('marketplace/indexLoggedIn.html')
    if not auth:
        template = loader.get_template('marketplace/indexMain.html')
    return HttpResponse(template.render(request))

def showProduct(request, num):
    url = 'http://exp-api:8000/product/' + str(num) + '/'
    req = urllib.request.Request('http://exp-api:8000/product/' + str(num) + '/')
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    resp = json.loads(resp_json)
    return render(request, 'marketplace/itemDetail.html', resp)

def productList(request):
    error_data = {
        "Error" : "Unable to load Product List"
    }
    not_auth = {
        "Error" : "Not Auth"
     }

    try:
        req = urllib.request.Request('http://exp-api:8000/viewAllProducts/')
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
        resp = json.loads(resp_json)
        resp = json.dumps(resp)
        #resp = resp.translate(None, '/')
        auth = request.COOKIES.get('auth')

        if not auth:
            return render(request, 'marketplace/productList.html', {"productList" : resp})

        return render(request, 'marketplace/productListLoggedIn.html', {"productList" : resp})
        #return JsonResponse(resp, safe=False)
    except:
        return render(request, 'marketplace/error.html', error_data)

def viewFormResults(request):
    template = loader.get_template('marketplace/viewFormResults.html')
    return HttpResponse(template.render(request))

@csrf_exempt
def createAccount(request):
    name = ''
    email = ''
    cardNumber = ''
    password = ''
    post_data = {}
    error_data = {"Error" : "Email already taken!"}
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            try:
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
                cardNumber = form.cleaned_data['cardNumber']
                password = form.cleaned_data['password']
                hashedPassword = make_password(password, salt=None, hasher='default')
                post_data = {
                    'name': name,
                    'email': email,
                    'cardNumber': cardNumber,
                    'password': hashedPassword
                }
                post_encoded = urllib.parse.urlencode(post_data).encode('utf-8')
                req = urllib.request.Request('http://exp-api:8000/customer/create/', data=post_encoded, method='POST')
                resp_json = urllib.request.urlopen(req).read().decode('utf-8')
                resp = json.loads(resp_json)
                return render(request, 'marketplace/account.html', post_data)
            except:
                return JsonResponse(error_data, safe=False)
    else:
        form = NameForm()
    return render(request, 'marketplace/account.html', post_data)

@csrf_exempt
def login(request):
    try:
        email = ''
        password = ''
        post_data = {}
        error_data = {"Error" : "Login Failed"}
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                post_data = {
                    'email': email,
                    'password': password
                    }
                post_encoded = urllib.parse.urlencode(post_data).encode('utf-8')
                req = urllib.request.Request('http://exp-api:8000/customer/login/', data=post_encoded, method='POST')
                resp_json = urllib.request.urlopen(req).read().decode('utf-8')
                resp = json.loads(resp_json)
                #if resp doesnt have ok set to true:
                if not resp or not resp['ok']:
                    #send back to login page
                    return JsonResponse(error_data)
                authenticator = resp['Authenticator']
                response = render(request, "marketplace/loggedin.html", post_data)
                response.set_cookie("auth", authenticator)
                return response
        else:
            form = LoginForm()
    except:
        return render(request, 'marketplace/error.html', error_data)

@csrf_exempt
def logout(request):
    error_data = {
        "Error" : "We had a problem logging you out, please try again"
    }
    try:
        auth = request.COOKIES.get("auth")
        post_auth = {
            "Authenticator": auth
        }
        post_encoded = urllib.parse.urlencode(post_auth).encode('utf-8')
        req = urllib.request.Request('http://exp-api:8000/customer/logout/', data=post_encoded, method='POST')
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
        resp = json.loads(resp_json)
        response = render(request, "marketplace/indexMain.html")
        if auth:
            response.delete_cookie("auth")
            return response
    except:
        return render(request, 'marketplace/indexMain.html')

@csrf_exempt
def createProduct(request):
    error_data = {
        "Error" : "Unable to create product, log in and try again"
    }
    try:
        auth = request.COOKIES.get('auth')
        if not auth:
            return render(request, 'marketplace/error.html', error_data)

        # if request.method == "GET":
        #     #fix url !!!!
        #     return render("loggedin.html")

        if request.method == "POST":
            product = request.POST['product']
            price = request.POST['price']
            post_data = {
                'product' : product,
                'price' : price,
                'auth' : auth
            }
            post_encoded = urllib.parse.urlencode(post_data).encode('utf-8')
            req = urllib.request.Request('http://exp-api:8000/product/create/', data=post_encoded, method='POST')
            resp_json = urllib.request.urlopen(req).read().decode('utf-8')
            resp = json.loads(resp_json)
            return render(request, 'marketplace/productRegistered.html', resp)
    except:
        return render(request, 'marketplace/error.html', error_data)

@csrf_exempt
def find(request):
    # auth = request.COOKIES.get('auth')
    # if not auth:
    #     return HttpResponse("NO auth")
    # query = ''
    post_data = {}
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['name']
            post_data = {
                'name': query
            }
            post_encoded = urllib.parse.urlencode(post_data).encode('utf-8')
            req = urllib.request.Request('http://exp-api:8000/search/', data=post_encoded, method='POST')
            resp_json = urllib.request.urlopen(req).read().decode('utf-8')
            resp = json.loads(resp_json)
            resp = json.dumps(resp)
            return render(request, 'marketplace/search.html', {"productList" : resp})
            # return render(request, 'marketplace/searchResults.html', resp)
            # return JsonResponse(resp, safe=False)
    else:
        form = SearchForm()
    # return render(request, 'marketplace/searchResults.html', post_data)
    return JsonResponse({'Error' : 'Input Required'})
