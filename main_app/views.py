from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import UserForm

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

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            error_message = 'invalid sign up - please try again'
    form = UserForm()
    context = {'form':form, 'error':error_message}
    return render(request, 'registration/signup.html', context)


""""""""""""""""""

class ProductCreate(CreateView):
    pass

class ProductUpdate(UpdateView):
    pass

class ProductDelete(DeleteView):
    pass


    