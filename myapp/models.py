from django.db import models
from django.contrib.auth.models import User  # https://docs.djangoproject.com/en/4.2/topics/auth/default/


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=200, default="nothing")
    last_name = models.CharField(max_length=200, default="nothing")
    email = models.CharField(max_length=200, default="nothing")
    username = models.CharField(max_length=200, default="nothing")
    password = models.CharField(max_length=200, default="nothing")