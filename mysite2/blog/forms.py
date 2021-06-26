from django import forms
from django.forms import formset_factory
from .models import Post, corona_help

class Postform(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'discreption',
            'catagoery',
            'sub_catagoery',
            'tags',
            'body',
        ]

class Corona_help_form(forms.ModelForm):
    class Meta:
        model = corona_help
        fields = [
            'title',
            'discreption',
            'contact'
        ]
