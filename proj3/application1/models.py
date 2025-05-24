from django.db import models

# Create your models here.
class  Products(models.Model):
    pid=models.IntegerField()
    pname=models.CharField(max_length=21)
    price=models.FloatField()
    company=models.CharField(max_length=21)
