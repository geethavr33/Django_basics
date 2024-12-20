from django.shortcuts import render
from .models import Student, Teacher  # Import Teacher model as well
from .serializer import Student_serializer
from django.db.models import Avg, Q, F, Sum, Count, ExpressionWrapper, FloatField
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
#from app_teacher.models import Teacher

# Create your views here.

class Crud_All_Student(APIView):
    def get(self, request, roll_no=None):
       
       
        try:
            #get student by iD
            if roll_no:
                try:
                    student = Student.objects.get(roll_no=roll_no)
                    serializer = Student_serializer(student)
                    return Response(serializer.data, status=status.HTTP_200_OK)
                except Student.DoesNotExist:
                    return Response({"error": "Student with the specific id not found"}, status=status.HTTP_400_BAD_REQUEST)
           
            #get all students
            student =Student.objects.all()
            serializer = Student_serializer(student, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
       
 
   
    def post(self, request):
        try:
            # Create a new student task
            serializer = Student_serializer(data=request.data)
           
            if serializer.is_valid():
                serializer.save()  # Save the new student
                return Response(serializer.data, status=status.HTTP_201_CREATED)
           
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
           
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
       
 
 
 
    def put(self, request, roll_no):
        
        try:
            student = Student.objects.get(roll_no=roll_no)
            serializer = Student_serializer(student, data=request.data, partial=True)
           
            if serializer.is_valid():
                serializer.save()  # Save the updated student
                return Response(serializer.data, status=status.HTTP_200_OK)
           
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
       
        except Student.DoesNotExist:
            return Response({"error": "Student with the specified roll number not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
 
 

    

#function to filter student by subject and Teacher
class StudentFilterBySubjectAndTeacherView(APIView):
    def get(self, request):
        # Get query parameters for filtering
        subject = request.query_params.get('subject', None)
        teacher_id = request.query_params.get('teacher_id', None)  # Changed from class_teacher to teacher_id

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
        
        # If filtering by teacher (changed to use teacher_id instead of class_teacher)
        elif teacher_id:
            students = Student.objects.filter(teacher_id=teacher_id).order_by('name')
            serializer = Student_serializer(students, many=True)
            data = serializer.data

        # If no filtering provided, return error
        else:
            return Response({"error": "Please provide either subject or teacher_id parameter"}, status=status.HTTP_400_BAD_REQUEST)

        # Return filtered data
        return Response(data, status=status.HTTP_200_OK)

        
#function for getting student details by id
   
# Function to get the topper
class TopperListView(APIView):
    def get(self, request):
        # Get the topper(s) with the highest total marks
        topper = Student.objects.order_by('-physics_marks', '-chemistry_marks', '-maths_marks').first()
        if topper:
            serializer = Student_serializer(topper)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"message": "No students found"}, status=status.HTTP_404_NOT_FOUND)

# Function to get all failed students
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

# function to get subject wise Failed list view
class SubjectWiseFailedListView(APIView):
    def get(self, request):
        subject = request.query_params.get('subject', None)
# pass mark is fixed ad 35
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

# Function to get Student above cutoff
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

# function to seperate students by average
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

#Function to get the best teacher


#Function to get the list of students who failed in a specific subject
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
            return Response({"error": "Invalid subject"}, status=status.HTTP_400_BAD_REQUEST)

        # Serialize the list of students who failed in the specified subject
        serializer = Student_serializer(failed_students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
# Function to get the list of students who passed in all subjects
class StudentsPassedInAllSubjectsView(APIView):
    def get(self, request):
        # Get students who passed in all subjects (assuming cutoff for passing is 35)
        passing_marks = 35
        passed_students = Student.objects.filter(
            Q(physics_marks__gte=passing_marks) &
            Q(chemistry_marks__gte=passing_marks) &
            Q(maths_marks__gte=passing_marks)
        ).order_by('name')
        
        serializer = Student_serializer(passed_students, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK) 

# Function to get the list of students who failed in all subjects
class StudentsFailedInAllSubjectsView(APIView):
    def get(self, request):
        # Get students who failed in all subjects (assuming cutoff for passing is 35)
        passing_marks = 35
        failed_students = Student.objects.filter(
            Q(physics_marks__lt=passing_marks) |
            Q(chemistry_marks__lt=passing_marks) |
            Q(maths_marks__lt=passing_marks)
        ).order_by('name')

        serializer = Student_serializer(failed_students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)    

# Function to get the list of students who passed in a specific subject
class StudentsPassedInSubjectView(APIView):
    def get(self, request, subject):
        # Set passing marks
        passing_marks = 35

        # Create filter condition based on the subject
        if subject == 'physics':
            passed_students = Student.objects.filter(physics_marks__gte=passing_marks)

        elif subject == 'chemistry':
            passed_students = Student.objects.filter(chemistry_marks__gte=passing_marks)
        elif subject == 'maths':
            passed_students = Student.objects.filter(maths_marks__gte=passing_marks)
        else:
            return Response({"error": "Invalid subject"}, status=status.HTTP_400_BAD_REQUEST)

        # Serialize the list of students who passed in the specified subject
        serializer = Student_serializer(passed_students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)   

# Function to get the list of students who passed in at least one subject
class StudentsPassedInAtLeastOneSubjectView(APIView):
    def get(self, request):
        # Get students who passed in at least one subject (assuming cutoff for passing is 35)
        passing_marks = 35
        passed_students = Student.objects.filter(
            Q(physics_marks__gte=passing_marks) |
            Q(chemistry_marks__gte=passing_marks) |
            Q(maths_marks__gte=passing_marks)
        ).order_by('name')

        serializer = Student_serializer(passed_students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)        

# Function to get the list of students who failed in at least one subject
class StudentsFailedInAtLeastOneSubjectView(APIView):
    def get(self, request):
        # Get students who failed in at least one subject (assuming cutoff for passing is 35)
        passing_marks = 35
        failed_students = Student.objects.filter(
            Q(physics_marks__lt=passing_marks) |
            Q(chemistry_marks__lt=passing_marks) |
            Q(maths_marks__lt=passing_marks)
        ).order_by('name')

        serializer = Student_serializer(failed_students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# Function to get the list of students who passed in a specific subject
class StudentsPassedInSubjectView(APIView):
    def get(self, request, subject):
        # Set passing marks
        passing_marks = 35

        # Create filter condition based on the subject
        if subject == 'physics':
            passed_students = Student.objects.filter(physics_marks__gte=passing_marks)

        elif subject == 'chemistry':
            passed_students = Student.objects.filter(chemistry_marks__gte=passing_marks)
        elif subject == 'maths':
            passed_students = Student.objects.filter(maths_marks__gte=passing_marks)
        else:
            return Response({"error": "Invalid subject"}, status=status.HTTP_400_BAD_REQUEST)

        # Serialize the list of students who passed in the specified subject
        serializer = Student_serializer(passed_students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK) 

# Function to get the list of students who passed in at least one subject
class StudentsPassedInAtLeastOneSubjectView(APIView):
    def get(self, request):
        # Get students who passed in at least one subject (assuming cutoff for passing is 35)
        passing_marks = 35
        passed_students = Student.objects.filter(
            Q(physics_marks__gte=passing_marks) |
            Q(chemistry_marks__gte=passing_marks) |
            Q(maths_marks__gte=passing_marks)
        ).order_by('name')

        serializer = Student_serializer(passed_students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)  

     
#function to get the Toppers
class TopperListView(APIView):
    def get(self, request):
        # Get the topper(s) with the highest total marks
        topper = Student.objects.order_by('-physics_marks', '-chemistry_marks', '-maths_marks').first()
        if topper:
            serializer = Student_serializer(topper)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"message": "No students found"}, status=status.HTTP_404_NOT_FOUND)

#Function to get Top Student details

class TopStudentsView(APIView):
    def get(self, request):
        # Calculate total marks for each student
        students = Student.objects.annotate(
            calculated_total_marks=F('physics_marks') + F('chemistry_marks') + F('maths_marks')
        ).order_by('-calculated_total_marks')[:10]  # Order by total marks and take the top 10

        # Serialize and return the student data
        top_students = students.values('roll_no', 'name', 'physics_marks', 'chemistry_marks', 'maths_marks', 'calculated_total_marks')
        return Response(top_students, status=status.HTTP_200_OK)


# sort student by class Teacher/
# students/<str:class_teacher>
class SortByTeacher(APIView):
    def get(self, request, class_teacher):
        try:
            # Fetch the teacher object (assuming teacher names are unique)
            teacher = Teacher.objects.get(name=class_teacher)

            # Filter students by teacher_id (foreign key)
            students = Student.objects.filter(teacher_id=teacher)

            # Serialize the student data
            serializer = Student_serializer(students, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)

        except Teacher.DoesNotExist:
            # Handle the case when the teacher does not exist
            return Response({"error": "Teacher not found"}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            # Handle any other exceptions
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
   