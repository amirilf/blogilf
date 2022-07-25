from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    birth_date = models.DateField(null=True,blank=True)
    bio = models.TextField(max_length=255,null=True,blank=True)
    email = models.EmailField(unique=True)
    profile = models.ImageField(upload_to='profiles',null=True,blank=True)


class UserFollowing(models.Model):
    user_id = models.ForeignKey(User, related_name="following",on_delete=models.CASCADE)
    following_user_id = models.ForeignKey(User, related_name="followers",on_delete=models.CASCADE)
