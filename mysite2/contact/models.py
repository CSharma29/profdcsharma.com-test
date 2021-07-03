from django.db import models

# Create your models here.


class Contact_Model(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    email = models.EmailField(max_length=300, null=False, blank=False)
    concern = models.TextField(max_length=700, null=False, blank=False)

    def __str__(self):
        return self.name


class News_Letter_Model(models.Model):
    email = models.EmailField(max_length=300)

    def __str__(self):
        return self.email
