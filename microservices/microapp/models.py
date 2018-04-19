from django.db import models
from django.http import JsonResponse


class Product(models.Model):
    product = models.CharField(max_length=60, unique=True)
    price = models.CharField(max_length=30)
    #unique email from customer auth lookup
    sellerEmail = models.CharField(max_length=100)
    def __str__(self):
        return self.product


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique = True)
    cardNumber = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

class Sale(models.Model):
    #this might cause an error!!!!!!
    #salesman = models.ForeignKey(Customer, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.product


class Authenticator(models.Model):
    user_id = models.CharField(max_length=100)
    authenticator = models.CharField(max_length=255, primary_key=True)
    date_created = models.CharField(max_length=100)

    def __str__(self):
        return self.user_id
