from django.shortcuts import render

# importing models (DB)
from .models import Student
from .serializer import Student_serializer
from django.db.models import Avg
from django.db.models import Q,F,Avg,Sum, Count,ExpressionWrapper, FloatField
# importing modules from rest_framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class StudentCrudView(APIView):
    # function to post data
    def post(self, request):
        serializer = Student_serializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()  # Save the student instance
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)       
    
    # function to list all data
    def get(self, request):
        students = Student.objects.all()  # Fetch all students
        serializer = Student_serializer(students, many=True)  # Serialize the list of students
        return Response(serializer.data, status=status.HTTP_200_OK)


class StudentFilterBySubjectAndTeacherView(APIView):
    def get(self, request):
        # Get query parameters for filtering
        subject = request.query_params.get('subject', None)
        class_teacher = request.query_params.get('class_teacher', None)

        if subject:
            if subject == 'physics':
                students = Student.objects.all().order_by('-physics_marks')
                data = [
                    {"roll_no": student.roll_no, "name": student.name, "physics_marks": student.physics_marks}
                    for student in students
                ]
            elif subject == 'chemistry':
                students = Student.objects.all().order_by('-chemistry_marks')
                data = [
                    {"roll_no": student.roll_no, "name": student.name, "chemistry_marks": student.chemistry_marks}
                    for student in students
                ]
            elif subject == 'maths':
                students = Student.objects.all().order_by('-maths_marks')
                data = [
                    {"roll_no": student.roll_no, "name": student.name, "maths_marks": student.maths_marks}
                    for student in students
                ]
            else:
                return Response({"error": "Invalid subject"}, status=status.HTTP_400_BAD_REQUEST)
        
        # If filtering by class teacher
        elif class_teacher:
            students = Student.objects.filter(class_teacher=class_teacher).order_by('name')
            serializer = Student_serializer(students, many=True)
            data = serializer.data

        # If no filtering provided, return error
        else:
            return Response({"error": "Please provide either subject or class_teacher parameter"}, status=status.HTTP_400_BAD_REQUEST)

        # Return filtered data
        return Response(data, status=status.HTTP_200_OK)\
        

class StudentDetailView(APIView):
    def get_student(self, roll_no):
        try:
            return Student.objects.get(roll_no=roll_no)
        except Student.DoesNotExist:
            return None

    def put(self, request, roll_no):
        # Find the student by roll_no
        student = self.get_student(roll_no)
        if student is None:
            return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)

        # Deserialize the request data and update student information
        serializer = Student_serializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()  # Save the updated student
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, roll_no):
        # Find the student by roll_no
        student = self.get_student(roll_no)
        if student is None:
            return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)

        # Delete the student
        student.delete()
        return Response({"message": "Student deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

class TopperListView(APIView):
    def get(self, request):
        # Get the topper(s) with the highest total marks
        topper = Student.objects.order_by('-physics_marks', '-chemistry_marks', '-maths_marks').first()
        if topper:
            serializer = Student_serializer(topper)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"message": "No students found"}, status=status.HTTP_404_NOT_FOUND)


class FailedStudentsListView(APIView):
    def get(self, request):
        # Get students who have failed in any subject (assuming cutoff for passing is 35)
        passing_marks = 35
        failed_students = Student.objects.filter(
            Q(physics_marks__lt=passing_marks) |
            Q(chemistry_marks__lt=passing_marks) |
            Q(maths_marks__lt=passing_marks)
        ).order_by('name')

        serializer = Student_serializer(failed_students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class SubjectWiseFailedListView(APIView):
    def get(self, request):
        subject = request.query_params.get('subject', None)

        if subject == 'physics':
            failed_students = Student.objects.filter(physics_marks__lt=35).order_by('name')
        elif subject == 'chemistry':
            failed_students = Student.objects.filter(chemistry_marks__lt=35).order_by('name')
        elif subject == 'maths':
            failed_students = Student.objects.filter(maths_marks__lt=35).order_by('name')
        else:
            return Response({"error": "Invalid or missing subject parameter"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = Student_serializer(failed_students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class StudentsAboveCutoffView(APIView):
    def get(self, request):
        cutoff = request.query_params.get('cutoff', 150)  # Default cutoff = 150
        cutoff = float(cutoff)

        # Annotate the queryset with total marks
        students = Student.objects.annotate(
            calculated_total_marks=ExpressionWrapper(
                F('physics_marks') + F('chemistry_marks') + F('maths_marks'),
                output_field=FloatField()
            )
        ).filter(calculated_total_marks__gte=cutoff).order_by('-calculated_total_marks')

        serializer = Student_serializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class StudentsAboveAndBelowAverageView(APIView):
    def get(self, request):
        # Calculate average total marks of all students
        all_students = Student.objects.all()
        total_sum = sum(student.total_marks for student in all_students)
        total_students = all_students.count()
        average_marks = total_sum / total_students if total_students > 0 else 0

        # Annotate students with their total marks
        students = Student.objects.annotate(
            calculated_total_marks=ExpressionWrapper(
                F('physics_marks') + F('chemistry_marks') + F('maths_marks'),
                output_field=FloatField()
            )
        )

        # Filter students based on average
        students_below_average = students.filter(calculated_total_marks__lt=average_marks).order_by('name')
        students_above_average = students.filter(calculated_total_marks__gte=average_marks).order_by('-calculated_total_marks')

        below_avg_serializer = Student_serializer(students_below_average, many=True)
        above_avg_serializer = Student_serializer(students_above_average, many=True)

        return Response({
            "average_marks": average_marks,
            "students_below_average": below_avg_serializer.data,
            "students_above_average": above_avg_serializer.data
        }, status=status.HTTP_200_OK)


class BestTeacherView(APIView):
    def get(self, request):
        # Get the teacher with the most students who passed all subjects (assuming cutoff for passing is 35)
        passing_marks = 35
        best_teacher_data = (
            Student.objects.filter(
                Q(physics_marks__gte=passing_marks) &
                Q(chemistry_marks__gte=passing_marks) &
                Q(maths_marks__gte=passing_marks)
            )
            .values('class_teacher')
            .annotate(
                passed_students=Count('roll_no'),   # Count of students who passed
                total_students=Count('class_teacher')  # Count of total students per teacher
            )
            .order_by('-passed_students')  # Order by count of passed students descending
        )
        
        # Get the teacher with the maximum number of passed students
        if best_teacher_data.exists():
            best_teacher = best_teacher_data.first()  # Get the best teacher's data
            response_data = {
                "best_teacher": best_teacher['class_teacher'],
                "passed_students": best_teacher['passed_students'],
                "total_students": best_teacher['total_students'],  # Total students for that teacher
            }
            return Response(response_data, status=status.HTTP_200_OK)

        return Response({"message": "No students found"}, status=status.HTTP_404_NOT_FOUND)





class StudentsFailedInSubjectView(APIView):
    def get(self, request, subject):
        # Set passing marks
        passing_marks = 35

        # Create filter condition based on the subject
        if subject == 'physics':
            failed_students = Student.objects.filter(physics_marks__lt=passing_marks)
        elif subject == 'chemistry':
            failed_students = Student.objects.filter(chemistry_marks__lt=passing_marks)
        elif subject == 'maths':
            failed_students = Student.objects.filter(maths_marks__lt=passing_marks)
        else:
            return Response({"error": "Invalid subject provided."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = Student_serializer(failed_students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class TopStudentsView(APIView):
    def get(self, request):
        # Calculate total marks for each student
        students = Student.objects.annotate(
            total_marks=F('physics_marks') + F('chemistry_marks') + F('maths_marks')
        ).order_by('-total_marks')[:10]  # Order by total marks and take the top 10
        
        # Serialize and return the student data
        top_students = students.values('roll_no', 'name', 'physics_marks', 'chemistry_marks', 'maths_marks', 'total_marks')
        return Response(top_students)