from django.shortcuts import render
from app3.models import StudentModel,DetailsModel
from django.views import View

class Student(View):
    def get(self,request):
        data=StudentModel.objects.all()
        return render(request,'a2.html',{'data':data})



class Detail(View):
    def get(self,request):
        data1=DetailsModel.objects.all()
        return render(request,'a2.html',{'data1':data1})