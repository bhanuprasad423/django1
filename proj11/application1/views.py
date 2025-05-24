from django.shortcuts import render
from application1.models import StudentModel
def StudentDetailsView(request):
    data = StudentModel.objects.all()
    context = {'data': data} 
    return render(request,'students.html',context)

def Student1DetailsView(request):
    data = StudentModel.objects.all()
    context = {'data': data}
    for i in data:
        total_marks =  i.sub1 + i.sub2 + i.sub3 + i.sub4 + i.sub5
        i.total_marks = total_marks
        percentage = total_marks/500 * 100
        i.percentage = percentage
        if percentage >= 90:
            i.grade = 'A'
        elif percentage >= 80:
            i.grade = 'B'
        elif percentage >= 70:
            i.grade = 'C'
        elif percentage >= 60:
            i.grade = 'D'
        else:
            i.grade = 'F'
    return render(request,'student1.html',context)
# Create your views here.
def Student2DetailsView(request):
    data = StudentModel.objects.all()
    context = {'data': data}
    for i in data:
        total_marks =  i.sub1 + i.sub2 + i.sub3 + i.sub4 + i.sub5
        i.total_marks = total_marks
        percentage = total_marks/500 * 100
        i.percentage = percentage
        if percentage >= 90:
            i.grade = 'A'
        elif percentage >= 80:
            i.grade = 'B'
        elif percentage >= 70:
            i.grade = 'C'
        elif percentage >= 60:
            i.grade = 'D'
        else:
            i.grade = 'F'
    return render(request,'student2.html',context)

def Student3DetailsView(request):
    data = StudentModel.objects.all()
    context = {'data': data}
    for i in data:
        total_marks =  i.sub1 + i.sub2 + i.sub3 + i.sub4 + i.sub5
        i.total_marks = total_marks
        percentage = total_marks/500 * 100
        i.percentage = percentage
        if percentage >= 90:
            i.grade = 'A'
        elif percentage >= 80:
            i.grade = 'B'
        elif percentage >= 70:
            i.grade = 'C'
        elif percentage >= 60:
            i.grade = 'D'
        else:
            i.grade = 'F'
    return render(request,'student3.html',context)

def Student4DetailsView(request):
    data = StudentModel.objects.all()
    context = {'data': data}
    for i in data:
        total_marks =  i.sub1 + i.sub2 + i.sub3 + i.sub4 + i.sub5
        i.total_marks = total_marks
        percentage = total_marks/500 * 100
        i.percentage = percentage
        if percentage >= 90:
            i.grade = 'A'
        elif percentage >= 80:
            i.grade = 'B'
        elif percentage >= 70:
            i.grade = 'C'
        elif percentage >= 60:
            i.grade = 'D'
        else:
            i.grade = 'F'
    return render(request,'student4.html',context)

def Student5DetailsView(request):
    data = StudentModel.objects.all()
    context = {'data': data}
    for i in data:
        total_marks =  i.sub1 + i.sub2 + i.sub3 + i.sub4 + i.sub5
        i.total_marks = total_marks
        percentage = total_marks/500 * 100
        i.percentage = percentage
        if percentage >= 90:
            i.grade = 'A'
        elif percentage >= 80:
            i.grade = 'B'
        elif percentage >= 70:
            i.grade = 'C'
        elif percentage >= 60:
            i.grade = 'D'
        else:
            i.grade = 'F'
    return render(request,'student5.html',context)