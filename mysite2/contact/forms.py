from django.db import models
from django import  forms
from .models import Contact_Model, News_Letter_Model

class Contact_Form(forms.ModelForm):
    class Meta:
        model = Contact_Model
        fields = [
            'name',
            'email',
            'concern',
        ]

class News_Letter_Form(forms.ModelForm):
    class Meta:
        model = News_Letter_Model
        fields = [
            'email'
        ]

