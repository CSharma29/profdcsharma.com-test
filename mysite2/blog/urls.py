from os import name
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.Home_view.as_view(), name='home'),
    path('wednesday_post/', views.wednesday_weekly.as_view(), name='wednesday_weekly'),
    path('khund_charcha/', views.khund_charcha.as_view(), name='khund_charcha'),
    path('english_dalies/', views.english_dalies.as_view(), name='english_dalies'),
    path('english_magazines/', views.english_magazines.as_view(), name='english_magazines'),
    path('punjabi_dalies/', views.punjabi_dalies.as_view(), name='punjabi_dalies'),
    path('punjabi_magazines/', views.punjabi_magazines.as_view(), name='punjabi_magazines'),
    path('new/', views.new_post.as_view(), name='add_new'),
    path('tag/<slug:slug>/', views.tagged, name='tagged'),
    path('post_detail/<slug:slug>/', views.post_detail, name='post_detail'),
    path('post/<slug:slug>/', views.Update_post.as_view(), name='update_post'),
    path('help/', views.corona_post.as_view(), name='corona_help'),
    path('list/', views.corona_help_posts.as_view(), name='help_list'),
    path('help_detail/<int:pk>', views.corona_help_detail_view.as_view(), name='help_detail'),


]