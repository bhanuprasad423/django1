from django.shortcuts import render,redirect
from application1.models import Student
from application1.forms import Stu_form

def x1(request):
    return render(request,'dashboard.html')


def x3(request):
    return render(request,'login.html')


def x(request):
    data=Student.objects.all()
    return render(request,'details.html',{'data':data})


def y(request):
    form=Stu_form()
    if request.method=="POST":
        form=Stu_form(request.POST)
        if form.is_valid():
            form.save()
        return redirect('details')
    return render(request,'register.html',{'form':form})
