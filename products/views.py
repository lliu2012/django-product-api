from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from .models import Product
from .forms import ProductForm, LoginForm


def home(request):
    return HttpResponseRedirect('/products/')


def index(request):
    products = Product.objects.all()
    form = ProductForm()
    return render(request, 'index.html', {'products': products, 'form': form})


def detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'detail.html', {'product': product})


# def post_product(request):
#     form = ProductForm(request.POST)
#     if form.is_valid():
#         product = Product( name = form.cleaned_data['name'],
#                            price = form.cleaned_data['price'],
#                            stack = form.cleaned_data['stack'],
#                            image_url = form.cleaned_data['image_url'])
#         product.save(commit=True)
#
#     return HttpResponseRedirect('/products')

def post_product(request):
    form = ProductForm(request.POST)
    if form.is_valid():
        product = form.save(commit=False)
        product.user = request.user
        product.save()
    return HttpResponseRedirect('/products/')


def profile(request, username):
    user = User.objects.get(username=username)
    products = Product.objects.filter(user=user)
    return render(request, 'profile.html',{'username': username, 'products': products})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username=u, password=p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/products/')
                else:
                    print("The account has been disabled!")
            else:
                print("The username and password were incorrect.")
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login/')


def new(request):
    form = ProductForm()
    return render(request, 'addNew.html', {'form': form})


def buy_product(request):
    product_id = request.GET.get('product_id', None)

    stack = 0
    if product_id:
        product = Product.objects.get(id=int(product_id))
        if product is not None:
            stack = product.stack - 1
            product.stack = stack
            product.save()

    return HttpResponse(stack)
