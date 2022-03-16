from math import degrees
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User



class Product(models.Model):
    name = models.CharField(max_length=50, null=True)
    description = models.TextField(max_length=250)
    price = models.FloatField()
    image_url = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)
    full_name = models.CharField(max_length=50, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(max_length=20, blank=False)
    address_line = models.CharField(max_length=40, blank=False)
    city = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=40, blank=False)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f"{self.id}, {self.date} and {self.user.id}"

class CartOrder(models.Model):
    order = models.ForeignKey(Order, null=True, blank=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product,null=True, blank=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return f"{self.quantity} and {self.product.name}"
