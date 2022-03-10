from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from .models import Product, ShoppingCart

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contactus(request):
    return render(request, 'contactus.html')

def location(request):
    return render(request, 'location.html')

def shoppingcart(request):
    pass

def products_index(request):
    products = Product.objects.all()
    return render(request, 'products/index.html', {
        'products': products,
    })

def products_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'products/detail.html', {
        'product': product,
    })

""""""""""""""""""

class ProductCreate(CreateView):
    pass

class ProductUpdate(UpdateView):
    pass

class ProductDelete(DeleteView):
    pass
