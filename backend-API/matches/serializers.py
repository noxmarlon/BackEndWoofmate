from rest_framework import serializers
from .models import Like, Match

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['like_type', 'pet', 'liked_user', 'timestamp']

    def validate(self, data):
        like_type = data.get('like_type')
        
        pet = data.get('pet')
        liked_user = data.get('liked_user') 

        if like_type == Like.DOGWALKER_LIKES_PET and not pet:
            raise serializers.ValidationError({"pet": "This field is required when liking a pet."})
        if like_type == Like.DOGOWNER_LIKES_DOGWALKER and not liked_user:
            print(liked_user)
            raise serializers.ValidationError({"liked_user": "This field is required when liking a dogwalker."})

        return data

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = ['id', 'user1', 'user2', 'pet', 'timestamp']
