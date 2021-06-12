from django.db import models
from django.db.models.base import Model
from django.template.defaultfilters import default
from taggit.managers import TaggableManager
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone
from ckeditor.fields import RichTextField
from uuid import uuid4
# Create your models here.

catagoery_choices = (
    ('wednesday_weekly', 'WEDNESDAY_WEEKLY'),
    ('english_dalies', 'ENGLISH_DALIES'),
    ('english_magazines', 'ENGLISH_MAGAZINES'),
    ('punjabi_dalies', 'PUNJABI_DALIES'),
    ('punjabi_magazines', 'PUNJABI_MAGAZINES'),
    ('khund_charcha', 'KHUND_CHARCHA'),
)

class Post(models.Model):
    title = models.CharField(max_length=100, null=True)
    discreption = models.CharField(max_length=130, null=True, blank=True)
    body = RichTextField(blank=True, null=True)
    catagoery = models.CharField(max_length = 100, choices=catagoery_choices, default='wednesday_weekly', null=True, blank=True)
    slug = models.SlugField(unique=True, max_length=100)
    tags = TaggableManager()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now())


    def publish(self):
        pass
    
    def __str__(self):
        return self.title

class corona_help(models.Model):
    title = models.CharField(max_length=300, blank=False, null=False)
    discreption = RichTextField(blank=False, null=False)
    contact = models.CharField(max_length =1000 ,blank=True, null=True)
    published_date = models.DateTimeField(default=timezone.now(), blank=True, null=True)

    def __str__(self):
        return self.title

class comments(models.Model):
    pass