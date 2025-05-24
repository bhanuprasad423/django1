from django.shortcuts import render
from application1.models import Mobiles
from application1.admin import Mobile_Admin
from application1.kk import Mobiles_form
# Create your views here.

def x(request):
    data=Mobiles.objects.all()
    return render(request,'index1.html',{'data':data})
def y(request):
    m=Mobiles_form()
    return render(request,'index1.html',{'m':m})