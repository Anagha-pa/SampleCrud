from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from .manager import CustomUserManager

class User(AbstractUser, PermissionsMixin):
    username = None
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=100, unique=True, null=True, blank=True)
    mobile = models.IntegerField(unique=True, null=True, blank=True)
    is_active = models.BooleanField(default=False, null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['mobile', 'first_name', 'last_name']

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.mobile}"

  
