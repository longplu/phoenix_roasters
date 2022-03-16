from django.shortcuts import render, redirect, reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, UpdateForm, SignupForm
from .models import Product


# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {
        'products': products
    })

def about(request):
    return render(request, 'about.html')

def contactus(request):
    return render(request, 'contactus.html')

def location(request):
    return render(request, 'location.html')


def signup(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        signup_form = SignupForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            username = signup_form.get('username')
            messages.success(
                request, "You have successfully created an account!")
            login(request, username)
            return redirect('home')
    else:
        signup_form = SignupForm()
    return render(request, 'registration/signup.html', context={"signup_form": signup_form})


def shoppingcarts_index(request):
    if request.user.is_authenticated:
        user=request.user
        order, created = Order.objects.get_or_create(user=user, complete=False)
        products = order.cartorder_set.all()
    else:
        products = []
    context = {'products': products}
    return render(request, 'shoppingcarts/index.html', context)

def shoppingcarts_add(request):
    quantity = int(request.POST.get('quantity'))
    shoppingcart = request.session.get('shoppingcarts_index', {})
    if id in shoppingcart:
        shoppingcart[id] = int(shoppingcart[id] + quantity)
    else:
        shoppingcart[id] = shoppingcart.get(id, quantity)
    request.session['shoppingcarts_index'] = shoppingcart
    return redirect(reverse('shoppingcarts_index'))

def shoppingcarts_update(request):
    quantity = int(request.POST.get('quantity'))
    shoppingcart = request.session.get('shoppingcarts_index', {})
    if quantity > 0:
        shoppingcart[id] = quantity
    else:
        shoppingcart.pop(id)

    request.session['shoppingcarts_index'] = shoppingcart
    return redirect(reverse('shoppingcarts_index'))


def products_detail(request, id):
    product = Product.objects.get(pk=id)
    return render(request, 'products/detail.html', {
        'product': product,
    })

""""""""""""""""""""""""""

class ProductCreate(CreateView):
    pass

class ProductUpdate(UpdateView):
    pass

class ProductDelete(DeleteView):
    pass


    