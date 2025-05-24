from django.db import models

class DetailsModel(models.Model):
    name=models.CharField(max_length=21)
    phone_no=models.PositiveBigIntegerField()
    address=models.TextField()


class StudentModel(DetailsModel):
    roll_no=models.PositiveSmallIntegerField()
    standard=models.IntegerField()