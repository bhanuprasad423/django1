from django.db import models

class std(models.Model):
    id=models.IntegerField().primary_key=True
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    address = models.CharField(max_length=50, default='unknown')

