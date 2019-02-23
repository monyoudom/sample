from django import forms
from .models import Information



class InformaitonForms(forms.ModelForm):
   class Meta:
        model = Information
        fields = ['email', 'phone_number', 'name']
