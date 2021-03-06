from django.db import models
from django.contrib.auth import get_user_model
from .fields import NonStrippingCharField

class Category(models.Model):
    slug = models.SlugField(unique=True)

class Article(models.Model):
    author     = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,related_name='articles')
    category   = models.ManyToManyField(Category,blank=True,related_name='categories') # article categories

    # Slug is unique but we set it up manually in the forms.py
    slug       = models.SlugField(max_length=100)
    
    title      = models.CharField(max_length=200)
    body       = models.TextField()
    status     = models.BooleanField(default=True)
    created    = models.DateTimeField(auto_now_add=True)
    updated    = models.DateTimeField(auto_now=True) # last update
    thumbnail  = models.ImageField(upload_to='articles')
    tags       = NonStrippingCharField(max_length=255,null=True,blank=True)
    views      = models.PositiveBigIntegerField(default=0)

    def get_tags(self):
        try:
            return self.tags.strip().split(' , ')
        except AttributeError:
            return None

    class Meta:
        ordering = ('-created', )