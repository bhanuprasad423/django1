from django.db import models

# Create your models here.
class StudentModel(models.Model):
    sname=models.CharField(max_length=21)
    roll_no=models.PositiveIntegerField()
    phone_no=models.IntegerField()
    standard=models.PositiveIntegerField()
    sub1=models.PositiveIntegerField()
    sub2=models.PositiveIntegerField()
    sub3=models.PositiveIntegerField()
    sub4=models.PositiveIntegerField()
    sub5=models.PositiveIntegerField()

