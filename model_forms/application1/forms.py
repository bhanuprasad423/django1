from django import forms
from application1.models import Student

class Student_form(forms.ModelForm):
    class Meta:
        model=Student
        fields="__all__"
        widgets={
            'stu_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the name'}),
            'roll_no':forms.NumberInput(attrs={'class':'form-control'}),
            'std':forms.NumberInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'marks':forms.NumberInput(attrs={'class':'form-control'}),
            'nick_name':forms.TextInput(attrs={'class':'form-control'}),
            'phone_no':forms.NumberInput(attrs={'class':'form-control'}),
        }