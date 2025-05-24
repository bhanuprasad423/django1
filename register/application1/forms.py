from django import forms
from application1.models import Student

class Stu_form(forms.ModelForm):
    class Meta:
        model=Student
        fields="__all__"
        widgets = {
            'rollno': forms.NumberInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'stu_class': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_no': forms.NumberInput(attrs={'class': 'form-control'}),   
            'address': forms.TextInput(attrs={'class': 'form-control'}),
        }