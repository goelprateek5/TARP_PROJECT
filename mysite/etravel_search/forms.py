from django import forms
from django.forms import ModelForm
from .models import Search


class SearchForm(ModelForm):
    class Meta:
        model=Search

        fields=['To','From','date']