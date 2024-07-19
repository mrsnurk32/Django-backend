from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, blank=True, null=True)
    middle_name = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self) -> str:
        return super().__str__()
