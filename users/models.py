from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(
        max_length=128,
        blank=True,
        null=True,
        unique=True,
    )
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=10)

    height = models.IntegerField(null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)
    dob = models.CharField(max_length=128, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "first_name", "last_name"]

    def __str__(self):
        return self.username
