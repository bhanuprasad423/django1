from django.shortcuts import render,redirect
from django.http import HttpResponse
from application1.models import Login,StudentsModel
from application1.forms import LoginForm,StudentForm
from django.db.models import Min,Max,Sum,Avg,Count



def x(request):
    form=LoginForm()
    return render(request,'loginpage.html',{'form':form})


def StudentView(request):
        students = StudentsModel.objects.all()
        return render(request,'student.html',{'students':students})




def StudentDetailsview(request,id):
    data=StudentsModel.objects.filter(id=id)
    return render(request,'studentdetails.html',{'data':data})



def updateView(request,id=id):
    student = StudentsModel.objects.get(id=id)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student')
    else:
        form = StudentForm(instance=student)
    return render(request, 'update.html', {'form': form, 'student': student})  


def delete(request,id):
    data=StudentsModel.objects.get(id=id)
    data.delete()
    return redirect('student')


def AddStudent(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student')
    else:
        form = StudentForm()
    return render(request, 'addstudent.html', {'form': form})


def filter1(request,standard):
    x=StudentsModel.objects.filter(standard=standard)
    return render(request,'student.html',{'x':x})
        
   
    