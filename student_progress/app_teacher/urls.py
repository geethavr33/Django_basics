from django.urls import path  # Importing path and include for URL routing
from .views import BestTeacherView,BestTeacherView,BestTeacherByDepartmentView, TeacherCrudOperations,TeacherPerformanceView,TotalStudentsForTeacherView
from django.http import HttpResponse


def home(request):
    return HttpResponse("Welcome to the Student Progress App!")
               
                                             

urlpatterns = [
    path('teachers/performance/', BestTeacherView.as_view(), name='teacher-performance'),  # URL for fetching the best teacher's performance
    path('teachers/',TeacherCrudOperations.as_view(),name='teacher'),  # URL for CRUD operations on teachers
    path('teachers/<int:teacher_id>/total/',TotalStudentsForTeacherView.as_view(),name='Total_StudentsOfTeacher'),
    path('teachers/<int:emp_id>/',TeacherCrudOperations.as_view(),name='teacherById'),  # URL for CRUD operations on teachers
    path('teachers/<int:teacher_id>/performance/', TeacherPerformanceView.as_view(), name='teacher-performance'),
    path('teachers/best/', BestTeacherView.as_view(), name='best-teacher'),
    path('teachers/best-by-department/', BestTeacherByDepartmentView.as_view(), name='best_teacher_by_department'),

]