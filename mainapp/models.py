from django.db import models


class ProductsCategory(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=30, unique=True, blank=True)
    descriptions = models.TextField(blank=True, null=True)


class Products(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=100, blank=True)
    price = models.PositiveIntegerField(blank=True)
    descriptions = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images_product', blank=True)
    quantity = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=30)
    category = models.ForeignKey(ProductsCategory, on_delete=models.CASCADE)
