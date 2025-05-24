from django.db import models

class UsersDeatils(models.Model):
    first_name=models.CharField(max_length=21)
    last_name=models.CharField(max_length=21)
    username=models.CharField(max_length=21)
    p1=models.CharField(max_length=21)
    p2=models.CharField(max_length=21)
    mobile_no=models.CharField(max_length=21)
    email=models.EmailField()

def __str__(self):
    return self.first_name+" "+self.last_name+" "+self.username+" "+self.p1+" "+self.p2+" "+self.mobile_no+"  "+self.email

