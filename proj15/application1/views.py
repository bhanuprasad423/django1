from django.shortcuts import render

def x(request):
    return render(request,'index.html')