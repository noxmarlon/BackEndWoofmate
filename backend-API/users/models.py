from django.contrib.auth.models import AbstractUser
from django.db import models

class Role(models.Model):
    DOGOWNER = 'dogowner'
    DOGWALKER = 'dogwalker'

    ROLE_CHOICES = [
        (DOGOWNER, 'Dog Owner'),
        (DOGWALKER, 'Dog Walker'),
    ]

    name = models.CharField(max_length=50, choices=ROLE_CHOICES, unique=True)

    def __str__(self):
        return self.get_name_display()

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    # make rol required
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.username
