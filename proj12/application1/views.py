from django.shortcuts import render
from application1.models import Student_Details


def StudentDetailsView(request):
    data=Student_Details.objects.all()
    context={'data':data}
    select_std=request.GET.get('std',)
    if select_std:
        students=Student_Details.objects.filter(standard=select_std)
    else:
        students=Student_Details.objects.all()
    context={
        'selected_std':select_std,
        'students':students,
    }
    return render(request,'student_details.html',context)


def StudentAll_DetailView(request,id):
    data=Student_Details.objects.all()
    total_marks=data.sub1+ data.sub2+data.sub3+data.sub4+data.sub5
    percentage=total_marks/5

    if percentage>90:
        data.grade='A'
    elif percentage>=80:
        data.grade='B'
    elif percentage>=70:
        data.grade='C'
    elif percentage >=60:
        data.grade='D'
    elif percentage >=50:
        data.grade='E'
    elif percentage <50:
        data.grade='Fail'

    return render(request,'studentalldetails.html')