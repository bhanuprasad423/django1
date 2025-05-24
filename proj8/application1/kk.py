from application1.models import Mobiles
from django import forms
class Mobiles_form(forms.ModelForm):
    class Meta:
        model=Mobiles
        fields="__all__"