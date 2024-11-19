from django import forms
from basic_app.models import UserData

class FormName(forms.ModelForm):
    class Meta:
        model = UserData  # Link the form to the UserData model
        fields = ['name', 'email', 'text']
