from django.urls import path,include
# importing from views.py
from .views import StudentCrudView, StudentFilterBySubjectAndTeacherView,StudentDetailView,TopperListView, StudentsAboveCutoffView, FailedStudentsListView,StudentsAboveAndBelowAverageView, SubjectWiseFailedListView,BestTeacherView, StudentsFailedInSubjectView,TopStudentsView,SortByTeacher,GetTeacherDetails
 

urlpatterns = [
 
    path('students/', StudentCrudView.as_view(), name='student-create'),
    path('students/filter/', StudentFilterBySubjectAndTeacherView.as_view(), name='student-filter-subject-teacher'),
    path('students/<int:roll_no>/', StudentDetailView.as_view(), name='student-detail'),
    path('students/toppers/', TopperListView.as_view(), name='toppers-list'),
    path('students/above_cutoff/', StudentsAboveCutoffView.as_view(), name='students-above-cutoff'),
    path('students/failed/', FailedStudentsListView.as_view(), name='failed-students'),
    path('students/average/', StudentsAboveAndBelowAverageView.as_view(), name='students-average'),
    path('students/subjectwise_failed/', SubjectWiseFailedListView.as_view(), name='subjectwise-failed-students'),
    path('teachers/performance/', BestTeacherView.as_view(), name='teacher-performance'),
    path('students/failed/<str:subject>/', StudentsFailedInSubjectView.as_view(), name='students-failed'),
    path('top-students/', TopStudentsView.as_view(), name='top_students'),
    path('students/<str:class_teacher>', SortByTeacher.as_view(), name='class_teacherName'),
    path('teacherdetails/<int:teacher_id>/', GetTeacherDetails.as_view(), name='teacher_details'),
    
]