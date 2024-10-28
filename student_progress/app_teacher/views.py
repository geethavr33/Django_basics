from django.shortcuts import render
from .models import  Teacher  # Import Teacher model as well
from app_student_progress.models import Student
from .serializer import  Teacher_serializer
from django.db.models import Avg, Q, F, Sum, Count, ExpressionWrapper, FloatField
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app_teacher.models import Teacher

from django.db.models import Q, Count
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

# View to find the best teacher with the most active students who passed all subjects
class BestTeacherView(APIView):
    def get(self, request):
        passing_marks = 35
        best_teacher_data = (
            Student.objects.filter(
                Q(is_active=True),
                Q(physics_marks__gte=passing_marks),
                Q(chemistry_marks__gte=passing_marks),
                Q(maths_marks__gte=passing_marks)
            )
            .values('teacher_id')  
            .annotate(
                passed_students=Count('roll_no'),  
                total_students=Count('teacher_id')  
            )
            .order_by('-passed_students')
        )

        if best_teacher_data.exists():
            best_teacher = best_teacher_data.first()
            teacher = Teacher.active_objects.get(emp_id=best_teacher['teacher_id'])
            response_data = {
                "best_teacher": teacher.name,
                "passed_students": best_teacher['passed_students'],
                "total_students": best_teacher['total_students'],
            }
            return Response(response_data, status=status.HTTP_200_OK)

        return Response({"message": "No active students found"}, status=status.HTTP_404_NOT_FOUND)

# View to retrieve details of a specific active teacher by ID
class GetTeacherDetails(APIView):
    def get(self, request, teacher_id):
        try:
            teacher = Teacher.active_objects.get(emp_id=teacher_id)
            serializer = Teacher_serializer(teacher)
            return Response({'Teacher': serializer.data}, status=status.HTTP_200_OK)
        except Teacher.DoesNotExist:
            return Response({'error': 'Teacher not found'}, status=status.HTTP_404_NOT_FOUND)

# View to list all active teachers
class TeacherListView(APIView):
    def get(self, request):
        teachers = Teacher.active_objects.all()
        serializer = Teacher_serializer(teachers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# View to create a new teacher
class TeacherCreateView(APIView):
    def post(self, request):
        serializer = Teacher_serializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# View to retrieve a specific active teacher by primary key
class TeacherRetrieveView(APIView):
    def get(self, request, pk):
        try:
            teacher = Teacher.active_objects.get(pk=pk)
            serializer = Teacher_serializer(teacher)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Teacher.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

# View to update a specific active teacher
class TeacherUpdateView(APIView):
    def put(self, request, pk):
        try:
            teacher = Teacher.active_objects.get(pk=pk)
            serializer = Teacher_serializer(teacher, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Teacher.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

# View to delete a specific active teacher
class TeacherDeleteView(APIView):
    def delete(self, request, pk):
        try:
            teacher = Teacher.active_objects.get(pk=pk)
            teacher.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Teacher.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

# New API to retrieve the total number of active students for a specific teacher
class TotalStudentsForTeacherView(APIView):
    def get(self, request, teacher_id):
        try:
            teacher = Teacher.active_objects.get(emp_id=teacher_id)
            total_students = Student.objects.filter(teacher_id=teacher, is_active=True).count()
            return Response({"teacher_name": teacher.name, "total_students": total_students}, status=status.HTTP_200_OK)
        except Teacher.DoesNotExist:
            return Response({"error": "Teacher not found"}, status=status.HTTP_404_NOT_FOUND)

# API to mark a teacher as inactive
class InactivateTeacherView(APIView):
    def put(self, request, teacher_id):
        try:
            teacher = Teacher.objects.get(emp_id=teacher_id)
            teacher.is_active = False
            teacher.save()
            return Response({"message": f"Teacher {teacher.name} marked as inactive."}, status=status.HTTP_200_OK)
        except Teacher.DoesNotExist:
            return Response({"error": "Teacher not found"}, status=status.HTTP_404_NOT_FOUND)