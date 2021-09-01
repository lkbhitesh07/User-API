from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import IntegerField
from .managers import CustomUserManager
# Create your models here.

class CustomUser(AbstractUser):
    company_name = models.CharField(max_length=50)
    age = models.IntegerField(default=0)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip = models.BigIntegerField(default=0)
    email = models.EmailField(unique=True)
    web = models.URLField(max_length=100)
    username = models.CharField(max_length=40, unique=False, default='')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
