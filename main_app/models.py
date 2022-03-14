from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image_url = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    full_name = models.CharField(max_length=50, blank=False)
    date = models.DateField()
    phone_number = models.CharField(max_length=20, blank=False)
    address_line = models.CharField(max_length=40, blank=False)
    city = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=40, blank=False)

    def __str__(self):
        return f"{self.id}, {self.date} and {self.user.id}"

class CartOrder(models.Model):
    order = models.ForeignKey(Order, null=False, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return f"{self.quantity} and {self.product.name}"
