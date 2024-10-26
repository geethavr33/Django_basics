from django.urls import path
from .views import  (
    DepartmentListView,
    DepartmentCreateView,
    DepartmentRetrieveView,
    DepartmentUpdateView,
    DepartmentDeleteView,
)

urlpatterns = [
    path('departments/', DepartmentListView.as_view(), name='department-list'),
    path('departments/create/', DepartmentCreateView.as_view(), name='department-create'),
    path('departments/<int:pk>/', DepartmentRetrieveView.as_view(), name='department-detail'),
    path('departments/<int:pk>/update/', DepartmentUpdateView.as_view(), name='department-update'),
    path('departments/<int:pk>/delete/', DepartmentDeleteView.as_view(), name='department-delete'),
]
