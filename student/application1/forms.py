from django import forms
from application1.models import StudentsModel,Login

class StudentForm(forms.ModelForm):
    class Meta:
        model=StudentsModel
        fields='__all__'

class LoginForm(forms.ModelForm):
    class Meta:
        model=Login
        fields='__all__'

    
