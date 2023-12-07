from django import forms
from .models import Category


class CreateCategoryForm(forms.Form):
    name = forms.CharField(max_length=200, label='Nome', widget=forms.TextInput(attrs={'class': 'form-control'}))
