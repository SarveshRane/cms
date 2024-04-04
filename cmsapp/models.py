

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser


class User_groups(AbstractUser):
    phone = models.CharField(max_length=10, blank=True)
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    pincode = models.CharField(max_length=6, blank=True)


class ContentItem(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField(max_length=300)
    summary = models.CharField(max_length=100, blank=True)
    categories = models.CharField(max_length=100, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
