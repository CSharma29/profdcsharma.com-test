from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.Home_view.as_view(), name='home'),
    path('new/', views.new_post.as_view(), name='add_new'),
    path('tag/<slug:slug>/', views.tagged, name='tagged'),
    path('post_detail/<slug:slug>/', views.post_detail, name='post_detail'),

]