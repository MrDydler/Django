from django import forms
from .models import RegistrationForm

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = RegistrationForm
        fields = '__all__'
