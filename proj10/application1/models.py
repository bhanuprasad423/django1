from django.db import models
class Products(models.Model):
    Pid=models.IntegerField()
    Pname=models.CharField(max_length=21)
    Price=models.FloatField()
    Company=models.CharField(max_length=21)
    M_date=models.DateField()
    Exp_date=models.DateField() 

class Customer(models.Model):
    Cid=models.IntegerField()
    Cname=models.CharField(max_length=21)
    Address=models.CharField(max_length=21)
    Mobile_Number=models.CharField(max_length=21)
    Email_Address=models.EmailField()
    product=models.ManyToManyField(Products)
