from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    role = models.ForeignKey('UserRole', related_name='role_of_user', on_delete=models.CASCADE, null=True, blank=True)


class UserRole(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
