from django.db import models
from users.models import CustomUser

class Pet(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='pets')
    petName = models.CharField(max_length=100)
    petType = models.CharField(max_length=100)
    petAge = models.PositiveIntegerField()
    petBreed = models.CharField(max_length=100)

    def __str__(self):
        return self.petName
