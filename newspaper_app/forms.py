from django import forms
from .models import newspaper_db

class newNewspaper_form(forms.ModelForm):
    class Meta:
        model = newspaper_db
        fields = ['title', 'description', 'author']
