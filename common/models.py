from django.db import models

# Create your models here.
class Customer(models.Model):
    customer_name = models.CharField(max_length=20)# table fields
    customer_email = models.CharField(max_length=30)
    customer_phone = models.BigIntegerField()
    customer_address = models.CharField(max_length=30)
    customer_gender = models.CharField(max_length=30)
    customer_password = models.CharField(max_length=30)
    customer_image = models.ImageField(upload_to='customer/',default='')

class Seller(models.Model):
    seller_name = models.CharField(max_length=20)
    seller_email = models.CharField(max_length=30)
    seller_phone = models.BigIntegerField()
    seller_address = models.CharField(max_length=100)
    company_name = models.CharField(max_length=20)
    acc_holdername = models.CharField(max_length=20)
    ifsc = models.CharField(max_length=20)
    branch = models.CharField(max_length=20)
    acc_number = models.BigIntegerField()
    seller_username = models.CharField(max_length=20)
    seller_password = models.CharField(max_length=20)
    seller_pic = models.ImageField(upload_to='seller/')