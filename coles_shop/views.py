from unicodedata import category

from django.db.models import QuerySet
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
    # reviews = Review.objects.filter(product_id=id)
    # products = Product.objects.filter(id=id)
    data = {
        'product': product,
        # 'reviews': reviews,
        # 'products': products,
    }

    return render(request, 'product.html', context=data)

def product_list(request):
    text = request.GET.get('search_text', '')
    products = Product.objects.filter(title__contains=text)
    # print(products)
    # reviews = Review.objects.all()
    try:
        price = int(request.GET.get('price', ''))
        products = products.filter(price=price)
    except:
        pass
    product = request.GET.get('product', '')
    product_selecter = Product.objects.all()
    print(request.GET)
    if product != '':
        print(product)
        products = Product.objects.filter(title=product)


    return render(request,'products.html', context={
        'products': products,
        'product': Product.objects.all(),
        'product_selecter': product_selecter
    })


def review_list(request):
    text = request.GET.get('search_text', '')
    reviews = Review.objects.all()

    # reviews = Review.objects.filter(text_contains=text, pub_date_year=2021).exclude(text='niger')
    # reviews = reviews.filter(date=date)
    return render(request, 'reviews.html', context={
        'reviews': reviews
    })