from django.db import models

# Create your models here.
class Mobiles(models.Model):
    img=models.ImageField(upload_to='images/')
    name=models.CharField(max_length=50)
    price=models.IntegerField()
    delivery=models.CharField(max_length=21)