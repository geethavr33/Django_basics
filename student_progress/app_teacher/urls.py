from django.urls import path, include  # Importing path and include for URL routing

from .views import (
 BestTeacherView,  # View for retrieving the teacher with the best performance
  GetTeacherDetails,                       # View for retrieving details of a specific teacher
  TeacherListView,                        # View for listing all teachers
  TeacherCreateView,                       # View for creating a new teacher record
  TeacherRetrieveView,                     # View for retrieving details of a specific teacher by primary key
  TeacherUpdateView,                       # View for updating an existing teacher's information
   TeacherDeleteView ,                       # View for deleting a teacher record
   TotalStudentsForTeacherView,             # View for retrieving the total number of students for a specific teacher
   InactivateTeacherView                    # View for inactivating a teacher's account
 )                                             

urlpatterns = [
    path('teachers/performance/', BestTeacherView.as_view(), name='teacher-performance'),  # URL for fetching the best teacher's performance
    path('teachers/', TeacherListView.as_view(), name='teacher-list'),  # URL for listing all teachers
    path('teachers/create/', TeacherCreateView.as_view(), name='teacher-create'),  # URL for creating a new teacher
    path('teachers/<int:pk>/', TeacherRetrieveView.as_view(), name='teacher-detail'),  # URL for fetching a specific teacher's details
    path('teachers/<int:pk>/update/', TeacherUpdateView.as_view(), name='teacher-update'),  # URL for updating teacher information
    path('teachers/<int:pk>/delete/', TeacherDeleteView.as_view(), name='teacher-delete'),  # URL for deleting a teacher record
    path('teacherdetails/<int:teacher_id>/', GetTeacherDetails.as_view(), name='teacher_details'),  # URL for fetching teacher details by ID
    path('teachers/<int:teacher_id>/total-students/', TotalStudentsForTeacherView.as_view(), name='total_students_for_teacher'),
    path('teachers/<int:teacher_id>/inactivate/', InactivateTeacherView.as_view(), name='inactivate_teacher'),

]