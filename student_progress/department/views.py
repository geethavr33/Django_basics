from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from app_student_progress.models import Department, Student
from app_student_progress.serializer import Student_serializer
from app_teacher.models import Teacher
from app_teacher.serializer import Teacher_serializer
from school.models import School
from school.serializers import SchoolSerializer
from .serializers import  DepartmentSerializer

# Class to handle GET (List all departments)
class DepartmentListView(APIView):
    def get(self, request):
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# Class to handle POST (Create a new department)
class DepartmentCreateView(APIView):
    def post(self, request):
        serializer = DepartmentSerializer(data=request.data,many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Class to handle GET (Retrieve a specific department by pk)
class DepartmentRetrieveView(APIView):
    def get(self, request, pk):
        try:
            department = Department.objects.get(pk=pk)
            serializer = DepartmentSerializer(department)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Department.DoesNotExist:
            return Response({'error': 'Department not found'}, status=status.HTTP_404_NOT_FOUND)

# Class to handle PUT (Update a specific department by pk)
class DepartmentUpdateView(APIView):
    def put(self, request, pk):
        try:
            department = Department.objects.get(pk=pk)
        except Department.DoesNotExist:
            return Response({'error': 'Department not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = DepartmentSerializer(department, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Class to handle DELETE (Delete a specific department by pk)
class DepartmentDeleteView(APIView):
    def delete(self, request, pk):
        try:
            department = Department.objects.get(pk=pk)
            department.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Department.DoesNotExist:
            return Response({'error': 'Department not found'}, status=status.HTTP_404_NOT_FOUND)

class DepartmentDetailView(APIView):
    # Get a department by ID (only active departments)
    def get(self, request, dept_id):
        try:
            department = Department.active_objects.get(dept_id=dept_id)
            serializer = DepartmentSerializer(department)
            return Response(serializer.data)
        except Department.DoesNotExist:
            return Response({"error": "Department not found or inactive"}, status=status.HTTP_404_NOT_FOUND)

    # Update a department by ID
    def put(self, request, dept_id):
        try:
            department = Department.active_objects.get(dept_id=dept_id)
            serializer = DepartmentSerializer(department, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Department.DoesNotExist:
            return Response({"error": "Department not found or inactive"}, status=status.HTTP_404_NOT_FOUND)

    # Delete a department by ID
    def delete(self, request, dept_id):
        try:
            department = Department.active_objects.get(dept_id=dept_id)
            department.is_active = False  # Soft delete
            department.save()
            return Response({"message": "Department deactivated"}, status=status.HTTP_204_NO_CONTENT)
        except Department.DoesNotExist:
            return Response({"error": "Department not found or inactive"}, status=status.HTTP_404_NOT_FOUND)

# Teachers under a specific Department (only active teachers)
class TeachersUnderDepartmentView(APIView):
    def get(self, request, dept_id):
        teachers = Teacher.active_objects.filter(depart_id=dept_id)
        serializer = Teacher_serializer(teachers, many=True)
        return Response({
            "count": teachers.count(),
            "active_teachers": serializer.data
        })

# Students under a specific Department (only active students)
class StudentsUnderDepartmentView(APIView):
    def get(self, request, dept_id):
        students = Student.active_objects.filter(teacher_id__depart_id=dept_id)
        serializer = Student_serializer(students, many=True)
        return Response({
            "count": students.count(),
            "active_students": serializer.data
        })

# Department Details including HOD, Teachers, Students, and School (only active records)
class DepartmentFullDetailView(APIView):
    def get(self, request, dept_id):
        try:
            department = Department.active_objects.get(dept_id=dept_id)
            hod = department.hod if department.hod.is_active else None
            teachers = Teacher.active_objects.filter(depart_id=dept_id)
            students = Student.active_objects.filter(teacher_id__depart_id=dept_id)

            return Response({
                "department": DepartmentSerializer(department).data,
                "hod": Teacher_serializer(hod).data if hod else None,
                "teachers": Teacher_serializer(teachers, many=True).data,
                "students": Student_serializer(students, many=True).data,
                "school": department.sc_id.name if department.sc_id else None
            })
        except Department.DoesNotExist:

            return Response({"error": "Department not found or inactive"}, status=status.HTTP_404_NOT_FOUND)
        

# API to mark a department as inactive
class InactivateDepartmentView(APIView):
    def put(self, request, department_id):
        try:
            department = Department.objects.get(dept_id=department_id)
            department.is_active = False
            department.save()
            return Response({"message": f"Department {department.name} marked as inactive."}, status=status.HTTP_200_OK)
        except Department.DoesNotExist:
            return Response({"error": "Department not found"}, status=status.HTTP_404_NOT_FOUND)
