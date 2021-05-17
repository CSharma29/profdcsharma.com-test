from django import forms
from django.forms import formset_factory
from .models import Post

class Postform(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'discreption',
            'tags',
            'body',
        ]
Postformset = formset_factory(Postform, extra=1)