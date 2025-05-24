from django.shortcuts import render,redirect
from application1.models import movies,web_series

def x(request):
    res={
        'ent':movies.objects.all(),
        'ent1':web_series.objects.all()
    }
    return render(request,'index.html',res)


def y(request):
    res={
            "data":movies.objects.all(),

    }

    return render(request,'movies.html',res)

def z(request):
    res={
        'data1':web_series.objects.all()
    }
    
    return render(request,'series.html',res)


def movie_details(request, id):
    data3=movies.objects.get(id=id)
    return render(request,'movie_details.html',{'data3':data3})


def series_details(request, id):
    data4=web_series.objects.get(id=id)
    return render(request,'series_details.html',{'data4':data4})

def dele(request, id):
    d5 = movies.objects.get(id=id)
    d5.delete()
    return redirect('movies')
