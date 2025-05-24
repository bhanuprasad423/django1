from django.shortcuts import render
from application2.models import StudentModel
def y(request):
    data1=StudentModel.objects.all()
    return render(request,'a2.html',{'data1':data1})