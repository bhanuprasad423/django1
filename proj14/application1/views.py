from django.shortcuts import render
from application1.models import Login
from application1.forms import Login_form
from django.http import HttpResponse
def x(request):
    return render(request,'a1.html')
def y(request):
    if request.method == 'POST':
        username1 = request.POST.get('a', '')
        password1 = request.POST.get('b', '')
        try:
            prasad = Login.objects.get(username=username1, password=password1)
            return render(request, 'index.html', {'prasad': prasad})
        except Login.DoesNotExist:
            return HttpResponse('<h1>Invalid username or password</h1>')
    else:
        return HttpResponse('<h1>Only POST method allowed</h1>')


def z(request):
  #  data=Login.objects.all()
   form = Login_form()
   return render(request,'b.html',{'form':form})