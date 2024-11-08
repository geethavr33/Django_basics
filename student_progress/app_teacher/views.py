from django.shortcuts import get_object_or_404, render
from app_student_progress.models import Student
from department.models import Department
from .serializer import  Teacher_serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Teacher
from django.db.models import Avg


class TeacherCrudOperations(APIView):
    def get(self, request, emp_id=None):
        try:
            if emp_id is not None:
                try:
                    teacher = Teacher.objects.get(emp_id=emp_id)
                    serializer = Teacher_serializer(teacher)
                    return Response(serializer.data)
                except Teacher.DoesNotExist:
                    return Response({"error":"id not found"},status=status.HTTP_400_BAD_REQUEST)
           
            # If no emp_id key, return all teachers
            else:
                teachers = Teacher.objects.all()
                serializer = Teacher_serializer(teachers, many=True)
                return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)        
 
    def post(self, request):
        try:
            serializer = Teacher_serializer(data=request.data)
           
            # Validate the input data
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
           
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
       
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
       
    def put(self, request, emp_id=None):
        try:
            # Attempt to retrieve the existing teacher record
            teacher = Teacher.objects.get(emp_id=emp_id)
        except Teacher.DoesNotExist:
            return Response({"message": "Teacher does not exist"}, status=status.HTTP_404_NOT_FOUND)
 
        # Initialize the serializer with the existing teacher's data and the updated data
        serializer = Teacher_serializer(teacher, data=request.data, partial=True)  # Use partial=True to allow partial updates
 
        # Validate the input data
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Teacher updated successfully", "data": serializer.data}, status=status.HTTP_200_OK)
       
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 

class TotalStudentsForTeacherView(APIView):
    def get(self, request, teacher_id):
        try:
            teacher = Teacher.objects.get(emp_id=teacher_id)
            total_students = Student.objects.filter(teacher_id=teacher, is_active=True).count()
            return Response({"teacher_name": teacher.name, "total_students": total_students}, status=status.HTTP_200_OK)
        except Teacher.DoesNotExist:
            return Response({"error": "Teacher not found"}, status=status.HTTP_404_NOT_FOUND)



class TeacherPerformanceView(APIView):
    def get(self, request, teacher_id):
        try:
            teacher = Teacher.objects.get(emp_id=teacher_id)
            students = Student.objects.filter(teacher_id=teacher, is_active=True)

            if not students.exists():
                return Response({"message": "No students assigned to this teacher."}, status=status.HTTP_200_OK)

            # Calculate average total marks of active students
            total_marks = sum(student.total_marks for student in students)
            average_marks = total_marks / students.count()
            
            # Assume performance is based on average marks
            performance = average_marks  # or another metric, if defined

            return Response({
                "teacher_name": teacher.name,
                "average_total_marks": average_marks,
                "performance": performance,
            }, status=status.HTTP_200_OK)
        
        except Teacher.DoesNotExist:
            return Response({"error": "Teacher not found"}, status=status.HTTP_404_NOT_FOUND)
        


class BestTeacherView(APIView):
    def get(self, request):
        try:
            # Get each teacher with the average total marks of their active students
            teachers = Teacher.objects.annotate(average_marks=Avg('student__total_marks'))
            
            # Filter out teachers who do not have students or have a null average
            teachers_with_avg = teachers.filter(average_marks__isnull=False)
            
            # Get the teacher with the highest average marks
            best_teacher = teachers_with_avg.order_by('-average_marks').first()
            
            if best_teacher:
                response_data = {
                    "teacher_name": best_teacher.name,
                    "teacher_id": best_teacher.emp_id,
                    "average_student_marks": best_teacher.average_marks,
                }
                return Response(response_data, status=status.HTTP_200_OK)
            else:
                return Response({"error": "No teachers with students found"}, status=status.HTTP_404_NOT_FOUND)
        
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class BestTeacherByDepartmentView(APIView):
    def get(self, request):
        # Dictionary to store top teacher for each department
        top_teachers = {}

        # Loop through each department
        for department in Department.objects.filter(is_active=True):
            # Get teachers in the current department
            teachers_in_dept = Teacher.objects.filter(dept_id=department)

            if teachers_in_dept.exists():
                # Calculate average student marks for each teacher in this department
                teacher_performance = teachers_in_dept.annotate(
                    avg_student_marks=Avg('student__total_marks')
                )

                # Find the teacher with the highest average marks
                best_teacher = teacher_performance.order_by('-avg_student_marks').first()

                # Add to result dictionary
                if best_teacher:
                    top_teachers[department.name] = {
                        "teacher_name": best_teacher.name,
                        "department": department.name,
                        "average_marks": best_teacher.avg_student_marks
                    }

        return Response(top_teachers, status=status.HTTP_200_OK)