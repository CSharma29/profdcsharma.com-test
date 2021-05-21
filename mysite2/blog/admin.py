from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import Post, corona_help
# Register your models here.

admin.site.register(Post)
admin.site.register(corona_help)

class MyAdminSite(AdminSite):
    site_header = 'Monty Python administration'

admin_site = MyAdminSite(name='pappuadmin')