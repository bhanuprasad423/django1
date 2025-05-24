from django.shortcuts import render
from application1.forms import user_forms
def x(request):
    form=user_forms()
    return render(request,'a1.html',{'form':form})