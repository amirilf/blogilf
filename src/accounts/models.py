from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    birth_date = models.DateField(null=True)
    bio = models.TextField(max_length=255,null=True)
    email = models.EmailField(unique=True)

class UserFollowing(models.Model):
    user_id = models.ForeignKey(User, related_name="following",on_delete=models.CASCADE)
    following_user_id = models.ForeignKey(User, related_name="followers",on_delete=models.CASCADE)
