from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = ("male", "Male")
        FEMALE = ("female", "Female")

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    nickname = models.CharField(max_length=15)
    gender = models.CharField(
        max_length=10,
        choices=GenderChoices.choices,
    )
    avatar = models.URLField(blank=True)

    def __str__(self):
        return self.nickname
