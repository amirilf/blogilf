from django.db import models
from account.models import User

class Category(models.Model):
    slug = models.SlugField(unique=True)

class Article(models.Model):
    author     = models.ForeignKey(User,on_delete=models.CASCADE,related_name='articles')
    category   = models.ManyToManyField(Category,blank=True,related_name='articles') # article categories
    slug       = models.SlugField(max_length=100)
    title      = models.CharField(max_length=200)
    body       = models.TextField()
    status     = models.BooleanField(default=True)
    created    = models.DateTimeField(auto_now_add=True)
    updated    = models.DateTimeField(auto_now=True) # last update
    thumbnail  = models.ImageField(upload_to='articles')