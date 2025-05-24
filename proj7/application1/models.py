from django.db import models

class Place(models.Model):
    name=models.CharField(max_length=21)
    address=models.CharField(max_length=21)
class Hotels(models.Model):
    place=models.OneToOneField(Place,on_delete=models.CASCADE, primary_key=True)
class Waiter(models.Model):
    name=models.CharField(max_length=21)
    email=models.EmailField()
    number=models.IntegerField()
    hotel=models.ForeignKey(Hotels,on_delete=models.CASCADE)


