from django.urls import path
from .views import DepartmentListCreateView, DepartmentRetrieveUpdateDeleteView

urlpatterns = [
    path('', DepartmentListCreateView.as_view(), name='department-list-create'),  # GET and POST
    path('<int:pk>/', DepartmentRetrieveUpdateDeleteView.as_view(), name='department-detail'),  # GET, PUT, DELETE
]
