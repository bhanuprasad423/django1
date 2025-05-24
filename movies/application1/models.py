from django.db import models
from datetime import datetime

class movies(models.Model):
    movie_id=models.IntegerField()
    movie_name=models.CharField(max_length=21)
    movie_frame=models.ImageField(upload_to='images/')
    budget=models.CharField(max_length=21)
    hero=models.CharField(max_length=21)
    director=models.CharField(max_length=21)
    description=models.CharField(max_length=300, default='No description available')
    rating=models.IntegerField()
    date=models.DateTimeField(default=datetime.now)


class web_series(models.Model):
    series_id=models.IntegerField()
    series_name=models.CharField(max_length=21)
    photo=models.ImageField(upload_to='images/')
    budget=models.CharField(max_length=21)
    hero=models.CharField(max_length=21)
    director=models.CharField(max_length=21)
    description=models.CharField(max_length=300, default='No description available')
    rating=models.IntegerField()