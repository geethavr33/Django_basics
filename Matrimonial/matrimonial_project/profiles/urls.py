from django.urls import path
from .views import CreateProfile, ProfileDetail
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('profiles/', CreateProfile.as_view(), name='create_profile'),
    path('profiles/<int:pk>/', ProfileDetail.as_view(), name='profile_detail'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
