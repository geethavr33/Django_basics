from django.urls import path
from .views import MatchMessageView,MatchMessagingView,UserMessagesView

urlpatterns = [
    path('send-match-messages/', MatchMessageView.as_view(), name='send-match-messages'),
    path('send-matching-message/', MatchMessagingView.as_view(), name='send_matching_message'),
    path('get-read-message/<int:user_id>/', UserMessagesView.as_view(), name='get-read-message'),

]
