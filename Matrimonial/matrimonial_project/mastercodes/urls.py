# urls.py
from django.urls import path
from .views import MasterCodeListView, MasterCodeDetailView

urlpatterns = [
    path('mastercodes/', MasterCodeListView.as_view(), name='mastercode-list'),
    path('mastercodes/<int:pk>/', MasterCodeDetailView.as_view(), name='mastercode-detail'),
]
