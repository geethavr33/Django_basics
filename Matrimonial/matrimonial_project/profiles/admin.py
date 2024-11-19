from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'age', 'gender', 'religion', 'status', 'created_on')
    search_fields = ('user__username', 'religion__display_text', 'caste__display_text')
    list_filter = ('status', 'gender', 'religion', 'created_on')
