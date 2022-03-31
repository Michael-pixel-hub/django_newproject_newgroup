from django.shortcuts import render
import json
from geekshop.settings import BASE_DIR
from mainapp.models import Products, ProductsCategory
# Create your views here.

def index(request):
    context = {
        "title": "Geekshop",
    }
    return render(request, 'mainapp/index.html', context)

def products(request):
    products = Products.objects.all()
    categories = ProductsCategory.objects.all()
    context = {
        "title": "Geekshop - Каталог",
        "products": products,
        "categories": categories,
    }
    return render(request, 'mainapp/products.html', context)