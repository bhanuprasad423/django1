from django.db import models 
class Reporters(models.Model):
    First_Name=models.CharField(max_length=21)
    Last_Name=models.CharField(max_length=21)
    Username=models.CharField(max_length=21)
    P1=models.CharField(max_length=21)
    P2=models.CharField(max_length=21)
    Mobile_Number=models.CharField(max_length=21)
    Email=models.EmailField() 

class Atricle(models.Model):    
    headline=models.CharField(max_length=29)
    public_date=models.DateField()
    reporter=models.ForeignKey(Reporters,on_delete=models.CASCADE)