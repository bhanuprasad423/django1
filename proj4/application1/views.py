from django.shortcuts import render
from application1.models import std
from django.http import HttpResponse

def x(request):
    data=std.objects.all()
    return render(request,'index1.html',{'data':data})

def insert_std(request):
    std.objects.create(id=5,name='Vikas',age='22',address='Mumbai')
    return HttpResponse("data Inserted")


def update_std(request,id):
    try:
        record=std.objects.get(id=id)
        record.name="sai"
        record.age=22
        record.address='Vizag'
        record.save()
        return HttpResponse(f"Record with id {id} updated successfully")
    except std.DoesNotExist:
            return HttpResponse(f"Record with id {id} not found")


def delete_std(request,id):
     try:
        record=std.objects.get(id=id)
        record.delete()
        return HttpResponse(f"Record of id {id} deleted successfully")
     except std.DoesNotExist:
          return HttpResponse(f"Record of id {id} not found")

def filt(request):  
     data=request.POST.get('x','')
     abc=std.objects.filter(name=data)
     return render(request,'index1.html',{'abc':abc})
def mm(request):
     return render(request,'index1.html')
     