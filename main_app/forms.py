from django import forms
from .models import State
from django.contrib.auth.models import User

class StateForm(forms.ModelForm):
    class Meta:
        model = State
        fields = ['name', 'motto', 'capital']

class UsernameForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']

