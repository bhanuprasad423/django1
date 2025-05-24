from django.db import models

class StudentModel(models.Model):
    stu_name=models.CharField(max_length=23)
    roll_no=models.PositiveSmallIntegerField()
    standard=models.CharField(max_length=21)