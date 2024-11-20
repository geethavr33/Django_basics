from django.urls import path
from .views import (
    BulkFestivalNotificationView,
    IncompleteProfileNotificationView,
    UnreadMessagesNotificationView,
    UnreadNotificationsView,
    UserNotificationsView
)

urlpatterns = [
    path('notifications/incomplete-profile/<int:user_id>/', IncompleteProfileNotificationView.as_view(), name='incomplete-profile-notification'),
    path('notifications/unread-messages/<int:user_id>/', UnreadMessagesNotificationView.as_view(), name='unread-messages-notification'),
    path('notifications/festival/', BulkFestivalNotificationView.as_view(), name='bulk_festival_notification'),
    path('notifications/unread/<int:user_id>/', UnreadNotificationsView.as_view(), name='unread-notifications'),
    path('notifications/<int:user_id>/', UserNotificationsView.as_view(), name='user_notifications'),

]
