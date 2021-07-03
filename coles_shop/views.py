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
    reviews = Review.objects.filter(product_id=id)
    # products = Product.objects.filter(id=id)
    data = {
        'product': product,
        'reviews': reviews,
        # 'products': products,
    }

    return render(request, 'product.html', context=data)

def product_list(request):
    text = request.GET.get('search_text', '')
    products = Product.objects.filter(title__contains=text)
    # reviews = Review.objects.all()
    try:
        price = int(request.GET.get('price', ''))
        products = products.filter(price=price)
    except:
        pass
    products = request.GET.get('products', '')
    # if products != '':
        # products = products.filter(category_id=int(category))


    return render(request,'products.html', context={
        'products': products,
        'reviews': Review.objects.all()
    })


# def review_list(request):
#     text = request.Get.get('search_text', '')
#     reviews = Review.objects.filter(text_contains=text, date__gt=2020).exclude(text='niger')
#
#     return render(request, 'reviews.html', context={
#         'reviews': reviews
#     })