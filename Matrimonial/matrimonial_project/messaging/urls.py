from django.urls import path
from .views import MatchMessageView

urlpatterns = [
    path('send-match-messages/', MatchMessageView.as_view(), name='send-match-messages'),
]
