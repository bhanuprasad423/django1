from django.shortcuts import render
from application1.models import Products
# Create your views here.
def Test_case1(request):
    data=Products.objects.all()
    return render(request,'index1.html',{'data': data})