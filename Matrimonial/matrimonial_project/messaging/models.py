from django.db import models
from user.models import User
from matches.models import Matching

class Messaging(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages_sent')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages_received')
    message_text = models.TextField()
    status = models.CharField(max_length=20, choices=[
        ('Sent', 'Sent'),
        ('Read', 'Read'),
        ('Deleted', 'Deleted')
    ])
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Message from {self.sender.username} to {self.receiver.username}"
