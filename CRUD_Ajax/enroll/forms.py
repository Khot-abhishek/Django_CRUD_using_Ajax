from django import forms
from .models import User


class StudentRegistration(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['name', 'email', 'password']
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control', 'id': 'name_id'}),
            'email' : forms.EmailInput(attrs={'class':'form-control', 'id': 'email_id'}),
            'password' : forms.PasswordInput(attrs={'class':'form-control', 'id' : 'password_id'})
        }