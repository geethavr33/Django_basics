from django.db import models
from user.models import User
from datetime import timedelta, date

class Subscription(models.Model):
    PLAN_CHOICES = [
        ('Free', 'Free'),
        ('Premium', 'Premium'),
    ]

    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Expired', 'Expired'),
        ('Suspended', 'Suspended'),
    ]
    id = models.BigAutoField(primary_key=True)  
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plan_type = models.CharField(max_length=50, choices=PLAN_CHOICES)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(null=True, blank=True)
   
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Active')

    def save(self, *args, **kwargs):
        if not self.end_date:
            self.end_date = self.start_date + timedelta(days=90)  # 3 months
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - {self.plan_type} ({self.status})"
