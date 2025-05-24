from django.db import models
from django.core.validators import MinLengthValidator,MaxLengthValidator,MinValueValidator,MaxValueValidator
from application1.validators import validate_name,validate_marks,validate_phone_no



class Student(models.Model):
    stu_name=models.CharField(max_length=21, validators=[validate_name])
    roll_no=models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(50)])
    std=models.PositiveIntegerField()
    address=models.TextField()
    marks=models.PositiveIntegerField(validators=[validate_marks])
    nick_name=models.CharField(max_length=15,validators=[MinLengthValidator(3),MaxLengthValidator(15)])
    phone_no=models.PositiveBigIntegerField(validators=[validate_phone_no])

