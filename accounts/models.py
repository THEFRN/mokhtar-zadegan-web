from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    phone_number = models.PositiveIntegerField(max_length=11)
    address = models.TextField()


    def __str__(self) -> str:
        return self.first_name
    

    

