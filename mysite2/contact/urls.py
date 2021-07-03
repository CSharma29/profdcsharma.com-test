from django import urls
from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    path('', views.Contact_View.as_view(), name ='contact_page'),
    path('sucess', views.Sucess_View, name = 'Sucess'),
    path('newsletter', views.News_Letter_View.as_view(), name = 'news_letter'),

]