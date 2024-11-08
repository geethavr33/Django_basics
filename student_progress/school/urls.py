from django.urls import path
from .views import SchoolListCreateView,SchoolStatusView,DepartmentsUnderSchoolView, TeachersUnderSchoolView, StudentsUnderSchoolView



urlpatterns = [
    path('schools/', SchoolListCreateView.as_view(), name='school-list-create'),  # For listing and creating schools
    path('schools/<int:sc_id>/', SchoolListCreateView.as_view(), name='school-update-create'),  # For listing and creating schools
    path('schools/<int:school_id>/departments/', DepartmentsUnderSchoolView.as_view(), name='departments_under_school'),
    path('schools/<int:school_id>/teachers/', TeachersUnderSchoolView.as_view(), name='teachers_under_school'),
    path('schools/<int:school_id>/students/', StudentsUnderSchoolView.as_view(), name='students_under_school'),
    path('schools/<str:status>/',SchoolStatusView.as_view(),name='school-status'),
 

]
