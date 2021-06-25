from os import name
from django.urls import path
from django.views.generic.base import RedirectView
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.Home_view.as_view(), name='home'),
    # Career tips view
    path('career_tips/', views.Career_Tips.as_view(), name='career_tips'),
    # Education
    path('education/', views.education.as_view(), name='education'),
    # life style view
    path('life_style/', views.life_style.as_view(), name='life_style'),
    # For behaviour
    path('behaviour/', views.Behaviour.as_view(), name='behaviour'),
    # for Psychology
    path('psychology/', views.Psychology.as_view(), name='psychology'),
    # for language
    path('language/', views.Language.as_view(), name='language'),
    path('new/', views.new_post.as_view(), name='add_new'),
    path('tag/<slug:slug>/', views.tagged, name='tagged'),
    path('post_detail/<slug:slug>/', views.post_detail, name='post_detail'),
    path('post/<slug:slug>/', views.Update_post.as_view(), name='update_post'),
    path('help/', views.corona_post.as_view(), name='corona_help'),
    path('list/', views.corona_help_posts.as_view(), name='help_list'),
    path('help_detail/<int:pk>', views.corona_help_detail_view.as_view(), name='help_detail'),
    path('about-us/', views.about_us.as_view(), name='about-us'),
]