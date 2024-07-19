from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Poll(models.Model):
    poll_name = models.CharField(max_length=128, blank=False, null=False)
    poll_number = models.IntegerField(blank=False, null=False, validators=[MinValueValidator(8), MaxValueValidator(1000)])

    def __str__(self) -> str:
        return self.poll_name