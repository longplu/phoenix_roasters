from email.policy import default
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User



class ShoppingCart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image_url = models.CharField(max_length=200)
    shopping_cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE, default='')

    def __str__(self):
        return f"{self.name}"


