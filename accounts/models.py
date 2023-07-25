from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=60, blank=True)
    last_name = models.CharField(max_length=60, blank=True)
    phone_number = models.PositiveIntegerField(null=True)
    address = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.first_name
    

    

