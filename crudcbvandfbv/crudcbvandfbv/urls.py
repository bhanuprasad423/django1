"""
URL configuration for crudcbvandfbv project.

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
from application1.views import (
    StudentListView, StudentCreateView,
    StudentUpdateView, StudentDeleteView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cbv/', StudentListView.as_view(), name='student_list_cbv'),
    path('cbv/create/', StudentCreateView.as_view(), name='student_create_cbv'),
    path('cbv/update/<int:pk>/', StudentUpdateView.as_view(), name='student_update_cbv'),
    path('cbv/delete/<int:pk>/', StudentDeleteView.as_view(), name='student_delete_cbv'),
]
