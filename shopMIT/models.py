from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default='Description')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="products", default="product.jpg")
