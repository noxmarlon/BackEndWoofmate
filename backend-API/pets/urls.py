from django.urls import path
from .views import PetListCreateView, PetDetailView, UserPetsListView, AllPetsListView

urlpatterns = [
    path('', PetListCreateView.as_view(), name='pet-list-create'),
    path('<int:pk>/', PetDetailView.as_view(), name='pet-detail'),
    path('my-pets/', UserPetsListView.as_view(), name='user-pets'),
    path('all-pets/', AllPetsListView.as_view(), name='all-pets'),
]
