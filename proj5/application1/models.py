from django.db import models

# Create your models here.
class employee(models.Model):
    eid=models.IntegerField()
    ename=models.CharField(max_length=21)
    sal=models.FloatField()
    company=models.CharField(max_length=21)
