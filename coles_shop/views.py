from django.http import HttpResponse
from django.shortcuts import render
from .models import Product, Category, Review


# Create your views here.

def hello_world(request):
    return HttpResponse(b'<h1>Hello world</h1>')

def index(request):
    products = Product.objects.all()
    data= {
        'title': "All products",
        'products': products
    }
    return render(request, 'index.html', context=data)

def product_item(request, id):
    product = Product.objects.get(id=id)
    reviews = Review.objects.filter(product_id=id)
    # products = Product.objects.filter(id=id)
    data = {
        'product': product,
        'reviews': reviews,
        # 'products': products,
    }

    return render(request, 'product.html', context=data)
