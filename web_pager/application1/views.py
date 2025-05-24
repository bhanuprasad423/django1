from django.shortcuts import render
from django.core.paginator import Paginator 
from application1.models import Product  




def product(request):
    p = Product.objects.all()
    paginator=Paginator(p,2)
    page_number=request.GET.get('page')
    x=paginator.get_page(page_number)
    return render(request,'a.html',{'x':x})
   