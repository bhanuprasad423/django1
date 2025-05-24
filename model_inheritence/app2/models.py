
from django.db import models

class DetailsModel(models.Model):
    name=models.CharField(max_length=21)
    phone_no=models.PositiveBigIntegerField()
    address=models.TextField()

    class Meta:
        abstract=True

class StudentModel(DetailsModel):
    roll_no=models.PositiveSmallIntegerField()
    standard=models.IntegerField()

class TeacherModel(DetailsModel):
    subject=models.CharField(max_length=21)
    salary=models.PositiveIntegerField()

