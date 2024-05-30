from rest_framework import generics, permissions
from .models import Pet
from .serializers import PetSerializer
from .permissions import IsOwner

class PetListCreateView(generics.ListCreateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Asigna el dueño de la mascota al usuario autenticado
        print("Headers:", self.request.headers)
        serializer.save(owner=self.request.user)

class PetDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

class UserPetsListView(generics.ListAPIView):
    serializer_class = PetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Filtrar las mascotas por el usuario autenticado
        return Pet.objects.filter(owner=self.request.user)

# class for get all pets of all users
class AllPetsListView(generics.ListAPIView):
    serializer_class = PetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Filtrar las mascotas por el usuario autenticado
        return Pet.objects.all()
