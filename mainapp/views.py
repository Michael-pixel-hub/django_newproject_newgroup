from django.shortcuts import render
import json
from geekshop.settings import BASE_DIR
# Create your views here.

def index(request):
    context = {
        "title": "Geekshop",
    }
    return render(request, 'mainapp/index.html', context)

def products(request):
    products_json = json.load(open (f'{BASE_DIR}/mainapp/fixtures/products.json', "r"))
    categories = ["Новинки", "Одежда", "Обувь", "Аксессуары", "Подарки"]
    context = {
        "title": "Geekshop - Каталог",
        "products": products_json['products'],
        "categories": categories,
    }
    return render(request, 'mainapp/products.html', context)