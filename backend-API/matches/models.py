from django.db import models
from users.models import CustomUser
from pets.models import Pet

class Like(models.Model):
    DOGWALKER_LIKES_PET = 'dogwalker_likes_pet'
    DOGOWNER_LIKES_DOGWALKER = 'dogowner_likes_dogwalker'

    LIKE_CHOICES = [
        (DOGWALKER_LIKES_PET, 'Dogwalker likes Pet'),
        (DOGOWNER_LIKES_DOGWALKER, 'Dogowner likes Dogwalker'),
    ]

    liker = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='likes_given')
    like_type = models.CharField(max_length=50, choices=LIKE_CHOICES)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, null=True, blank=True)
    liked_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='likes_received', null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('liker', 'like_type', 'liked_user')

class Match(models.Model):
    user1 = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='matches_as_user1')
    user2 = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='matches_as_user2')
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user1', 'user2', 'pet')
