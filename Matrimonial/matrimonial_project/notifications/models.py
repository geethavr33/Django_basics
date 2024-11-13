from django.db import models
from user.models import User
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notification_type = models.CharField(max_length=50)
    message = models.TextField()
    status = models.CharField(max_length=20, choices=[
        ('Unread', 'Unread'),
        ('Read', 'Read')
    ])
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Notification for {self.user.username} - {self.notification_type}"
