from django.db import models

class Student_Details(models.Model):
    stu_name=models.CharField(max_length=21)
    stu_rollno=models.IntegerField()
    stu_addr=models.CharField(max_length=21)
    stu_phone=models.IntegerField()
    standard=models.PositiveIntegerField()
    sub1=models.PositiveIntegerField()
    sub2=models.PositiveIntegerField()    
    sub3=models.PositiveIntegerField()    
    sub4=models.PositiveIntegerField()
    sub5=models.PositiveIntegerField()
