from django.urls import path
from .views import UnreadNotificationsView, IncompleteProfileNotificationView, UnreadMessagesView

urlpatterns = [
    path('notifications/unread/<int:user_id>/', UnreadNotificationsView.as_view(), name='unread_notifications'),
    path('notifications/incomplete-profile/<int:user_id>/', IncompleteProfileNotificationView.as_view(), name='incomplete_profile_notifications'),
    path('messages/unread/<int:user_id>/', UnreadMessagesView.as_view(), name='unread_messages'),
]
