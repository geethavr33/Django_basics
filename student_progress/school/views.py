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
    def get(self, request, sc_id=None):
 
        try:
            # If a primary key is provided, retrieve a specific school
            if sc_id:  
                try:
                    school = School.objects.get(sc_id=sc_id)
                    serializer = SchoolSerializer(school)
                    return Response(serializer.data)
                except School.DoesNotExist:
                    return Response({"error":"School with the specific id not found"}, status=status.HTTP_400_BAD_REQUEST)
 
            # If no primary key, return all schools
            schools = School.objects.all()
            serializer = SchoolSerializer(schools, many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
       
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
 
    def post(self, request):
        # Create a new school
        serializer = SchoolSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, sc_id=None):
        try:
            school = School.objects.get(sc_id=sc_id)
        except School.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
 
        serializer = SchoolSerializer(school, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

   
# View for retrieving, updating, and deleting a specific school

   
# School Detail View (Retrieve, Update, Delete)


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
        teachers = Teacher.objects.filter(sc_id=school_id)
        serializer = Teacher_serializer(teachers, many=True)
        return Response({
            "count": teachers.count(),
            "active_teachers": serializer.data
        })

# Students Under School View (only active students)
class StudentsUnderSchoolView(APIView):
    def get(self, request, school_id):
        students = Student.objects.filter(teacher_id__sc_id=school_id)
        serializer = Student_serializer(students, many=True)
        return Response({
            "count": students.count(),
            "active_students": serializer.data
        })

class SchoolStatusView(APIView):
    def get(self, request, status):
        if status == 'active':
            schools = School.objects.filter(is_active=True)
        elif status == 'inactive':
            schools = School.objects.filter(is_active=False)
        else:
            return Response({"error": "Invalid status. Use 'active' or 'inactive'."}, status=400)
       
        serializer = SchoolSerializer(schools, many=True)
        return Response(serializer.data)
 