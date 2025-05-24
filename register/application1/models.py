from django.db import models

class Student(models.Model):
    rollno=models.IntegerField()
    name=models.CharField(max_length=21)
    stu_class=models.CharField(max_length=21)
    phone_no=models.IntegerField()
    address=models.CharField()
    