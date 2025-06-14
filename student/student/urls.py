"""
URL configuration for student project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from application1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',views.x),
    path('update/<int:id>/',views.updateView, name='update'),
    path('delete/<int:id>/',views.delete, name='delete'),
    path('student/',views.StudentView, name='student'),
    path('studentdetails/<int:id>',views.StudentDetailsview, name='studentdetail'),
    path('addstudent/',views.AddStudent, name='addstudent'),
    path('filter/<str:standard>/',views.filter1,name='filter')

]
