from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

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

def products_index(request):
    pass

def products_detail(request):
    pass

def shoppingcart(request):
    pass

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            error_message = 'invalid sign up - please try again'
    form = UserCreationForm()
    context = {'form':form, 'error':error_message}
    return render(request, 'registration/signup.html', context)

""""""""""""""""""

class ProductCreate(CreateView):
    pass

class ProductUpdate(UpdateView):
    pass

class ProductDelete(DeleteView):
    pass