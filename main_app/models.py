from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

SIZES = (
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
)

HOTORICED = (
    ('H', 'Hot'),
    ('I', 'Iced'),
)

class ShoppingCart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Favorite(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class AddOn(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    image_url = models.CharField(max_length=200)    
    
    def __str__(self):
        return f"{self.name}"

class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    sub_category = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    size = models.CharField(max_length=1, choices=SIZES, default=SIZES[0][0])
    hot_or_iced = models.CharField(max_length=1, choices=HOTORICED, default=HOTORICED[0][0])
    price = models.IntegerField()
    image_url = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"


