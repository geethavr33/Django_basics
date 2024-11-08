from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app_student_progress.models import Department, Student
from app_student_progress.serializer import Student_serializer
from app_teacher.models import Teacher
from app_teacher.serializer import Teacher_serializer
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
            department = Department.objects.get(dept_id=dept_id)
            department.is_active = False  # Soft delete
            department.save()
            return Response({"message": "Department deactivated"}, status=status.HTTP_204_NO_CONTENT)
        except Department.DoesNotExist:
            return Response({"error": "Department not found or inactive"}, status=status.HTTP_404_NOT_FOUND)

# Teachers under a specific Department (only active teachers)
class TeachersUnderDepartmentView(APIView):
    def get(self, request, dept_id):
        teachers = Teacher.objects.filter(dept_id=dept_id)
        serializer = Teacher_serializer(teachers, many=True)
        return Response({
            "count": teachers.count(),
            "active_teachers": serializer.data
        })

# Students under a specific Department (only active students)
class StudentsUnderDepartmentView(APIView):
    def get(self, request, dept_id):
        students = Student.objects.filter(teacher_id__dept_id=dept_id)
        serializer = Student_serializer(students, many=True)
        return Response({
            "count": students.count(),
            "active_students": serializer.data
        })


class InactivateDepartmentView(APIView):
    def put(self, request, department_id):
        try:
            # Fetch the department and update its active status
            updated_count = Department.objects.filter(dept_id=department_id).update(is_active=False)

            # Check if any department was updated
            if updated_count == 0:
                return Response({"error": "Department not found"}, status=status.HTTP_404_NOT_FOUND)

            # Fetch the related teachers
            teachers = Teacher.objects.filter(dept_id=department_id)

            # Inactivate related teachers (if dept_id is a ForeignKey)
            teachers.update(is_active=False)

            # Clear the ManyToMany relationship (if applicable)
            for teacher in teachers:
                teacher.dept_id.clear()  # Remove all department links for this teacher

            # Inactivate related students
            Student.objects.filter(teacher_id__dept_id=department_id).update(teacher_id=None, is_active=False)

            return Response({"message": "Department and all related entities marked as inactive."}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)