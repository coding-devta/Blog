from django.db import models
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField
from .helpers import *


class profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_verified = models.BooleanField(default = False)
    token = models.CharField(max_length = 100)
    def __str__(self):
       return self.user

class blogmodel(models.Model):
    title = models.CharField(max_length=10000)
    description = FroalaField()
    slug = models.SlugField(max_length=500, null = True , blank = True)
    user = models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'blog')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
       return self.title


    def save(self, *args, **kwargs):
        self.slug = slug_generator(self.title)
        super(blogmodel, self).save(*args, **kwargs)
