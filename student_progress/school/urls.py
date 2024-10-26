from django.urls import path
from .views import SchoolListCreateView, SchoolRetrieveUpdateDeleteView

urlpatterns = [
    path('schools/', SchoolListCreateView.as_view(), name='school-list-create'),  # For listing and creating schools
    path('schools/<int:pk>/', SchoolRetrieveUpdateDeleteView.as_view(), name='school-retrieve-update-delete'),  # For retrieving, updating, and deleting a specific school

]
