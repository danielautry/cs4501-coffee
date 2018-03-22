from django.db import models
from django.http import JsonResponse


class CoffeeProduct(models.Model):
    coffeeType = models.CharField(max_length=60)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.coffeeType


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    cardNumber = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Sale(models.Model):
    salesman = models.CharField(max_length=100)
    amount = models.IntegerField(default=0)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    coffeeProduct = models.ForeignKey(CoffeeProduct, on_delete=models.CASCADE)

    def __str__(self):
        return self.salesman
