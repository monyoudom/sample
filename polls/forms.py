from django import forms
from .models import Information



class InformaitonForms(forms.ModelForm):
   class Meta:
        model = Information
        fields = ['email', 'phone_number', 'name']
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
