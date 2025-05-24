from django.shortcuts import render
from app2.models import StudentModel, TeacherModel

def x(request):
    data=StudentModel.objects.all()
    return render(request,'a1.html',{'data':data})

def y(request):
    data1=TeacherModel.objects.all()
    return render(request,'a1.html',{'data1':data1})