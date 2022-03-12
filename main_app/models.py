import email
from email.policy import default
from itertools import product
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f"{self.name}"

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image_url = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"

class ShoppingCart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    transaction_id = models.CharField(max_length=150, null=True)
    date_order = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.customer} on {self.date_order}"

class CartOrder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    shoppingcart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=0, null=True)
    date_add = models.DateTimeField()
