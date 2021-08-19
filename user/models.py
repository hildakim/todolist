from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    nickname = models.CharField(max_length=100, default="아기사자")
    birth = models.DateField(max_length=10, null=True, blank=True)