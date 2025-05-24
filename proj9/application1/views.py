from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

# Create your views here.
def x(request):
    return render(request,'test1.html')

class Product(View):
    def x(request):
        return render(request,'test1.html')