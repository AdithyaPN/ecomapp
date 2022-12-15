from django.db import models
from common.models import Seller

# Create your models here.
class Product(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=50)
    product_description = models.CharField(max_length=100)
    product_number = models.BigIntegerField()
    product_price = models.FloatField()
    current_stock = models.BigIntegerField(default=1)
    product_image = models.ImageField(upload_to='product')
    