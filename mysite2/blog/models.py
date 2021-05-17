from django.db import models
from taggit.managers import TaggableManager
from django.db.models.signals import pre_save
from django.dispatch import receiver
from ckeditor.fields import RichTextField
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=300, null=True)
    discreption = models.CharField(max_length=700, null=True, blank=True)
    body = RichTextField(blank=True, null=True)
    slug = models.SlugField(unique=True, max_length=100)
    tags = TaggableManager()


    def publish(self):
        pass
    
    def __str__(self):
        return self.title


# Dealing with the unique slug generation problem

def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = 'SLUG'
