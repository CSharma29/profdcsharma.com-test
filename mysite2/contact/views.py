from django.shortcuts import render
from django.views.generic import TemplateView, View
from .forms import Contact_Form, News_Letter_Form
from django.shortcuts import redirect, render
# Create your views here.


class Contact_View(View):
    tempalte_name = "contact/contact_us.html"
    form_class = Contact_Form
    initial = {
        'name': 'Please enter your name',
        'email': 'Please enter your email',
        'concern': 'Please tell us your concern',
    }

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.tempalte_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            contact_us = form.save(commit=False)
            contact_us.save()
            return redirect('contact:Sucess')
        return render(request, self.template_name, {'form': form})


def Sucess_View(request):
    return render(request, "contact/sucess.html")


class News_Letter_View(View):
    template_name = "contact/news_letter.html"
    form_class = News_Letter_Form
    initial = {
        'email': 'Please enter your email here'
    }

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            news_letter = form.save(commit=False)
            news_letter.save()
            return redirect('contact:Sucess')
        return render(request, self.template_name, {'form': form})
