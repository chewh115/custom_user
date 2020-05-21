from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class MyUser(AbstractUser):
    display_name = models.CharField(max_length=50, blank=True)
    homepage = models.URLField(max_length=50, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)