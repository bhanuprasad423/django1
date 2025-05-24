from django.shortcuts import render
from application1.models import employee

# Create your views here.
def x(request):
    list_display=employee.objects.all()
    return render(request,'index1.html',{'data': list_display})
