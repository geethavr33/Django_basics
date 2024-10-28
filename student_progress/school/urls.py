from django.urls import path
from .views import SchoolListCreateView, SchoolRetrieveUpdateDeleteView,SchoolDetailView, DepartmentsUnderSchoolView, TeachersUnderSchoolView, StudentsUnderSchoolView

from . import views

urlpatterns = [
    path('schools/', SchoolListCreateView.as_view(), name='school-list-create'),  # For listing and creating schools
    path('schools/<int:pk>/', SchoolRetrieveUpdateDeleteView.as_view(), name='school-retrieve-update-delete'),  # For retrieving, updating, and deleting a specific school
    path('schools/<int:school_id>/', SchoolDetailView.as_view, name='school_detail'),
    path('schools/<int:school_id>/departments/', DepartmentsUnderSchoolView.as_view(), name='departments_under_school'),
    path('schools/<int:school_id>/teachers/', TeachersUnderSchoolView.as_view(), name='teachers_under_school'),
    path('schools/<int:school_id>/students/', StudentsUnderSchoolView.as_view(), name='students_under_school'),

]
