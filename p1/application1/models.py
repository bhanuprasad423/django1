from django.db import models

class Profile(models.Model):
    name=models.CharField(max_length=21)
    username=models.CharField(max_length=21)
    password=models.CharField(max_length=21)