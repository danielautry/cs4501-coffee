from django.db import models
from django.http import JsonResponse


class CoffeeProduct(models.Model):
    coffeeType = models.CharField(max_length=60, unique=True)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.coffeeType


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique = True)
    cardNumber = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

class Sale(models.Model):
    salesman = models.CharField(max_length=100)
    amount = models.IntegerField(default=0)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    coffeeProduct = models.ForeignKey(CoffeeProduct, on_delete=models.CASCADE)

    def __str__(self):
        return self.salesman

class Review(models.Model):
    text = models.CharField(max_length=400)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    coffeeProduct = models.ForeignKey(CoffeeProduct, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

class Authenticator(models.Model):
    user_id = models.CharField(max_length=100)
    authenticator = models.CharField(max_length=255, primary_key=True)
    date_created = models.CharField(max_length=100)

    def __str__(self):
        return self.user_id
