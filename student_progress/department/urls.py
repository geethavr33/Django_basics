from django.urls import path  # Import path for defining URL patterns
from .views import  (
    DepartmentListView,      # View for listing all departments
    DepartmentCreateView,    # View for creating a new department
    DepartmentRetrieveView,  # View for retrieving details of a specific department
    DepartmentUpdateView,    # View for updating an existing department
    DepartmentDeleteView,    # View for deleting a specific department
    DepartmentDetailView,
    TeachersUnderDepartmentView,
    StudentsUnderDepartmentView,
    DepartmentFullDetailView,
    InactivateDepartmentView
)

# Define URL patterns for the department-related endpoints
urlpatterns = [
    # Route to list all departments
    path('departments/', DepartmentListView.as_view(), name='department-list'),

    # Route to create a new department
    path('departments/create/', DepartmentCreateView.as_view(), name='department-create'),

    # Route to retrieve details of a specific department using its primary key (pk)
    path('departments/<int:pk>/', DepartmentRetrieveView.as_view(), name='department-detail'),

    # Route to update an existing department using its primary key (pk)
    path('departments/<int:pk>/update/', DepartmentUpdateView.as_view(), name='department-update'),

    # Route to delete a specific department using its primary key (pk)
    path('departments/<int:pk>/delete/', DepartmentDeleteView.as_view(), name='department-delete'),

    path('departments/<int:dept_id>/', DepartmentDetailView.as_view(), name='department_detail'),
    path('departments/<int:dept_id>/teachers/', TeachersUnderDepartmentView.as_view(), name='teachers_under_department'),
    path('departments/<int:dept_id>/students/', StudentsUnderDepartmentView.as_view(), name='students_under_department'),
    path('departments/<int:dept_id>/details/', DepartmentFullDetailView.as_view(), name='department_full_detail'),
    path('departments/<int:department_id>/inactivate/', InactivateDepartmentView.as_view(), name='inactivate_department'),

]
