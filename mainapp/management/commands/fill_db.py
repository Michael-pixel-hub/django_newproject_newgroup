import json
from django.core.management.base import BaseCommand

from authapp.models import User
from mainapp.models import Products, ProductsCategory


def load_from_json(file_name):
    with open(file_name, mode='r', encoding='utf-8') as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        User.objects.create_superuser(username='Misha', email='kurashevmichael@gmail.com', password='0000')
        categories = load_from_json('mainapp/fixtures/products_category.json')
        ProductsCategory.objects.all().delete()
        for category in categories:
            cat = category.get("fields")
            cat['id'] = category.get('pk')
            new_category = ProductsCategory(**cat)
            new_category.save()

        products = load_from_json('mainapp/fixtures/products.json')
        Products.objects.all().delete()
        for product in products:
            prod = product.get("fields")
            category = prod.get('category')
            _category = ProductsCategory.objects.get(id=category)
            prod['category'] = _category
            new_category = Products(**prod)
            new_category.save()