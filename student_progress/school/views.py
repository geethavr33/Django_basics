from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from app_student_progress.models import Student
from app_student_progress.serializer import Student_serializer
from app_teacher.models import Teacher
from app_teacher.serializer import Teacher_serializer
from department.models import Department
from department.serializers import DepartmentSerializer
from .models import School
from .serializers import SchoolSerializer

# View for listing and creating schools
class SchoolListCreateView(APIView):
    def get(self, request):
        # List all schools
        schools = School.objects.all()
        serializer = SchoolSerializer(schools, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        # Create a new school
        serializer = SchoolSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# View for retrieving, updating, and deleting a specific school
class SchoolRetrieveUpdateDeleteView(APIView):
    def get(self, request, pk):
        # Retrieve a specific school
        try:
            school = School.objects.get(school_id=pk)
            serializer = SchoolSerializer(school)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except School.DoesNotExist:
            return Response({"error": "School not found."}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        # Update a specific school
        try:
            school = School.objects.get(school_id=pk)
        except School.DoesNotExist:
            return Response({"error": "School not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = SchoolSerializer(school, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        # Delete a specific school
        try:
            school = School.objects.get(school_id=pk)
            school.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except School.DoesNotExist:
            return Response({"error": "School not found."}, status=status.HTTP_404_NOT_FOUND)


# School Detail View (Retrieve, Update, Delete)
class SchoolDetailView(APIView):
    def get(self, request, school_id):
        school = get_object_or_404(School, school_id=school_id)
        serializer = SchoolSerializer(school)
        return Response(serializer.data)

    def put(self, request, school_id):
        school = get_object_or_404(School, school_id=school_id)
        serializer = SchoolSerializer(school, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, school_id):
        school = get_object_or_404(School, school_id=school_id)
        school.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Departments Under School View (only active departments)
class DepartmentsUnderSchoolView(APIView):
    def get(self, request, school_id):
        departments = Department.active_objects.filter(sc_id=school_id)
        serializer = DepartmentSerializer(departments, many=True)
        return Response({
            "count": departments.count(),
            "active_departments": serializer.data
        })

# Teachers Under School View (only active teachers)
class TeachersUnderSchoolView(APIView):
    def get(self, request, school_id):
        teachers = Teacher.active_objects.filter(sc_id=school_id)
        serializer = Teacher_serializer(teachers, many=True)
        return Response({
            "count": teachers.count(),
            "active_teachers": serializer.data
        })

# Students Under School View (only active students)
class StudentsUnderSchoolView(APIView):
    def get(self, request, school_id):
        students = Student.active_objects.filter(teacher_id__sc_id=school_id)
        serializer = Student_serializer(students, many=True)
        return Response({
            "count": students.count(),
            "active_students": serializer.data
        })