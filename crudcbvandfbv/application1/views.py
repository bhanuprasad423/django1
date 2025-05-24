from django.shortcuts import render, redirect
from application1.models import Student
from application1.forms import StudentForm
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

class StudentListView(ListView):
    model=Student
    template_name='list.html'
    context_object_name='students'

class StudentUpdateView(UpdateView):
    form_class=StudentForm
    template_name='form.html'
    success_url=reverse_lazy('student_list_cbv')

class StudentCreateView(CreateView):
    form_class=StudentForm
    template_name='form.html'
    success_url=reverse_lazy('student_list_cbv')

class StudentDeleteView(DeleteView):
    model=Student
    template_name='student_delete.html'
    success_url=reverse_lazy('student_list_cbv')