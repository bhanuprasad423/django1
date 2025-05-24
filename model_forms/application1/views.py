from django.shortcuts import render, redirect
from django.http import HttpResponse
from application1.forms import Student_form
from application1.models import Student

def StudentFormView(request):
    if request.method == 'POST':
        form=Student_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('inserted')
        return render(request,'student.html',{'form':form})

    form = Student_form()
    return render(request,'student.html',{'form':form})

def UpdateStudentView(request,id):
    data=Student.objects.get(id=id)
    form=Student_form(request.POST,instance=data)
    if form.is_valid():
        form.save()
        return HttpResponse('updated')
    form = Student_form(instance=data)
    return render (request,'update.html',{'form':form})


def StudentDetails(request):
    data=Student.objects.all()
    return render(request,'details.html',{'data':data})

def DeleteStudent(request,id):
    data=Student.objects.get(id=id)
    data.delete()
    return redirect('student_list')
