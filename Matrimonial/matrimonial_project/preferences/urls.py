from django.urls import path
from .views import CreatePreferences, PreferencesDetail

urlpatterns = [
    path('preferences/', CreatePreferences.as_view(), name='preferences-list'),
    path('preferences/<int:pk>/', PreferencesDetail.as_view(), name='preferences-detail'),
]
