from django.db import models
from django.core.validators import MinLengthValidator,MaxLengthValidator,MinValueValidator,MaxValueValidator
from application1.validators import validate_name,validate_phone,validate_marks,validate_username,validate_password


class StudentsModel(models.Model):
    sname = models.CharField(max_length=20,validators=[validate_name])
    roll_no = models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(50)])
    phone_no = models.PositiveBigIntegerField(validators=[validate_phone])
    standard = models.TextField()
    sub1 = models.PositiveIntegerField(validators=[validate_marks])
    sub2 = models.PositiveIntegerField(validators=[validate_marks])
    sub3 = models.PositiveIntegerField(validators=[validate_marks])
    sub4 = models.PositiveIntegerField(validators=[validate_marks])
    sub5 = models.PositiveIntegerField(validators=[validate_marks])
    
    

    def __str__(self):
        return self.sname
    
    def total_marks(self):
        return self.sub1 + self.sub2 + self.sub3 + self.sub4 + self.sub5
    
    def percentage(self):
        return self.total_marks()//5
    

class Login(models.Model):
    username=models.CharField(max_length=21,validators=[validate_username])
    password=models.CharField(max_length=21,validators=[validate_password])