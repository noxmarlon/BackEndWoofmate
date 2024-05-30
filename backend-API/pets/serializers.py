from rest_framework import serializers
from .models import Pet

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ['id', 'owner', 'petName', 'petType', 'petAge', 'petBreed']
        read_only_fields = ['owner']  # Asegura que el campo 'owner' es de solo lectura
