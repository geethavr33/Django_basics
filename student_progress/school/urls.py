from django.urls import path
from .views import SchoolListCreateView, SchoolRetrieveUpdateDeleteView

urlpatterns = [
    path('', SchoolListCreateView.as_view(), name='school-list-create'),  # GET and POST
    path('<int:pk>/', SchoolRetrieveUpdateDeleteView.as_view(), name='school-detail'),  # GET, PUT, DELETE
    
]
