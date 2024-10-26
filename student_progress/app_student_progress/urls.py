from django.urls import path, include  # Importing path and include for URL routing
# Importing view classes for handling requests
from .views import (
    StudentCrudView,                         # View for creating, updating, and deleting student records
    StudentFilterBySubjectAndTeacherView,   # View for filtering students by subject and teacher
    StudentDetailView,                       # View for retrieving details of a specific student
    TopperListView,                          # View for listing students with the highest marks (toppers)
    StudentsAboveCutoffView,                # View for listing students above a certain cutoff score
    FailedStudentsListView,                  # View for listing students who failed
    StudentsAboveAndBelowAverageView,        # View for comparing students above and below average marks
    SubjectWiseFailedListView,               # View for listing students who failed in specific subjects
    BestTeacherView,                         # View for retrieving the teacher with the best performance
    StudentsFailedInSubjectView,             # View for listing students who failed in a specific subject
    TopStudentsView,                         # View for listing top students based on performance
    SortByTeacher,                          # View for sorting students by class teacher
    GetTeacherDetails,                       # View for retrieving details of a specific teacher
    TeacherListView,                        # View for listing all teachers
    TeacherCreateView,                       # View for creating a new teacher record
    TeacherRetrieveView,                     # View for retrieving details of a specific teacher by primary key
    TeacherUpdateView,                       # View for updating an existing teacher's information
    TeacherDeleteView                        # View for deleting a teacher record
)

# Defining the URL patterns for the app
urlpatterns = [
    path('students/', StudentCrudView.as_view(), name='student-create'),  # URL for student CRUD operations
    path('students/filter/', StudentFilterBySubjectAndTeacherView.as_view(), name='student-filter-subject-teacher'),  # URL for filtering students
    path('students/<int:roll_no>/', StudentDetailView.as_view(), name='student-detail'),  # URL for fetching student details by roll number
    path('students/toppers/', TopperListView.as_view(), name='toppers-list'),  # URL for listing toppers
    path('students/above_cutoff/', StudentsAboveCutoffView.as_view(), name='students-above-cutoff'),  # URL for listing students above cutoff
    path('students/failed/', FailedStudentsListView.as_view(), name='failed-students'),  # URL for listing failed students
    path('students/average/', StudentsAboveAndBelowAverageView.as_view(), name='students-average'),  # URL for average comparison
    path('students/subjectwise_failed/', SubjectWiseFailedListView.as_view(), name='subjectwise-failed-students'),  # URL for subject-wise failures
    path('teachers/performance/', BestTeacherView.as_view(), name='teacher-performance'),  # URL for fetching the best teacher's performance
    path('students/failed/<str:subject>/', StudentsFailedInSubjectView.as_view(), name='students-failed'),  # URL for listing students failed in a specific subject
    path('top-students/', TopStudentsView.as_view(), name='top_students'),  # URL for listing top-performing students
    path('students/<str:class_teacher>/', SortByTeacher.as_view(), name='class_teacherName'),  # URL for sorting students by class teacher
    path('teacherdetails/<int:teacher_id>/', GetTeacherDetails.as_view(), name='teacher_details'),  # URL for fetching teacher details by ID
    path('teachers/', TeacherListView.as_view(), name='teacher-list'),  # URL for listing all teachers
    path('teachers/create/', TeacherCreateView.as_view(), name='teacher-create'),  # URL for creating a new teacher
    path('teachers/<int:pk>/', TeacherRetrieveView.as_view(), name='teacher-detail'),  # URL for fetching a specific teacher's details
    path('teachers/<int:pk>/update/', TeacherUpdateView.as_view(), name='teacher-update'),  # URL for updating teacher information
    path('teachers/<int:pk>/delete/', TeacherDeleteView.as_view(), name='teacher-delete'),  # URL for deleting a teacher record
]
