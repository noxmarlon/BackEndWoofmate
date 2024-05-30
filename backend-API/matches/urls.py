from django.urls import path
from .views import LikeCreateView, MatchListView

urlpatterns = [
    path('like/', LikeCreateView.as_view(), name='like-create'),
    path('matches/', MatchListView.as_view(), name='match-list'),
]
