"""proj11 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
    path('student/',views.StudentDetailsView, name='student'),
    path('student1/',views.Student1DetailsView, name='student1'),
    path('student2/',views.Student2DetailsView, name='student2'),
    path('student3/',views.Student3DetailsView, name='student3'),
    path('student4/',views.Student4DetailsView, name='student4'),
    path('student5/',views.Student5DetailsView, name='student5'),
]
