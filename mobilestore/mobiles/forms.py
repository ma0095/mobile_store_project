from django import forms
from mobiles.models import Mobile

class MobileCreateForm(forms.ModelForm):
    class Meta:
        model=Mobile
        fields="__all__"
