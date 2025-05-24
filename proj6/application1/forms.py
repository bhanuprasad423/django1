from django import forms
class user_forms(forms.Form):
    first_name=forms.CharField(max_length=21,label='first name')
    last_name=forms.CharField(max_length=21,label='last name')
    password=forms.CharField(max_length=21,label='password')