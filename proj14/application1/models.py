from django.db import models
class Login(models.Model):
    username=models.CharField(max_length=21)
    password=models.CharField(max_length=21)
