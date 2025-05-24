from django.shortcuts import render
from application1.models import StudentModel


def x(request):
    data=StudentModel.objects.all()
    return render(request,'a1.html',{'data':data})
