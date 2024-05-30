from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Like, Match
from .serializers import LikeSerializer, MatchSerializer
from rest_framework.exceptions import ValidationError
# Create your views here.

class LikeCreateView(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]
    

    def perform_create(self, serializer):
        user = self.request.user
        like_type = serializer.validated_data.get('like_type')
        pet = serializer.validated_data.get('pet', None)
        liked_user = serializer.validated_data.get('liked_user', None)

        # Check if user already liked the pet or dogwalker
        if like_type == Like.DOGWALKER_LIKES_PET:
            if Like.objects.filter(liker=user, like_type=like_type, pet=pet).exists():
                raise ValidationError({"pet": "You already liked this pet."})
        elif like_type == Like.DOGOWNER_LIKES_DOGWALKER:
            if Like.objects.filter(liker=user, like_type=like_type, liked_user=liked_user).exists():
                raise ValidationError({"liked_user": "You already liked this dogwalker."})
        
        # Asignar liker y liked_user automáticamente
        if like_type == Like.DOGWALKER_LIKES_PET:
            if not pet:
                raise ValidationError({"pet": "This field is required when liking a pet."})
            liked_user = pet.owner
            serializer.save(liker=user, liked_user=liked_user)
        elif like_type == Like.DOGOWNER_LIKES_DOGWALKER:
            if not liked_user:
                raise ValidationError({"liked_user": "This field is required when liking a dogwalker."})
            serializer.save(liker=user, pet=None)

        # Check for mutual like
        if like_type == Like.DOGWALKER_LIKES_PET:
            opposite_like_type = Like.DOGOWNER_LIKES_DOGWALKER
            opposite_like = Like.objects.filter(
                liker=liked_user,
                like_type=opposite_like_type,
                liked_user=user
            ).first()
        else:
            opposite_like_type = Like.DOGWALKER_LIKES_PET
            opposite_like = Like.objects.filter(
                liker=liked_user,
                like_type=opposite_like_type,
                # pet=pet
            ).first()

        if opposite_like:
            Match.objects.create(
                user1=user,
                user2=liked_user,
                pet=pet if pet else opposite_like.pet
            )

class MatchListView(generics.ListAPIView):
    serializer_class = MatchSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Match.objects.filter(user1=self.request.user) | Match.objects.filter(user2=self.request.user)
