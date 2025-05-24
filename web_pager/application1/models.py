from django.db import models

class Product(models.Model):
    product_id=models.IntegerField()
    product_name=models.CharField(max_length=21)
    price=models.FloatField()
    brand=models.CharField(max_length=21)
   