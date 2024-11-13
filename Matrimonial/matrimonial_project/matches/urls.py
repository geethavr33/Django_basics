from django.urls import path
from .views import MatchUsersAPIView

urlpatterns = [
    path('match/', MatchUsersAPIView.as_view(), name='match-users'),
]
