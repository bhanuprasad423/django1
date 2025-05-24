from application1.models import Login
from django import forms

class Login_form(forms.ModelForm):
    class Meta:
        model=Login
        fields="__all__"