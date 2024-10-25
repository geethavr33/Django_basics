# Refining the Student and Teacher Models
### Today, I worked on enhancing the Student and Teacher models by adding new fields and relationships.

### Tasks:

* Added performance field to Student model to track performance based on marks.
* Modified Teacher model to calculate their performance by averaging student marks.
* Set up automatic updates for the teacher's performance whenever student marks are changed.
Code Changes:
# models.py

```python

class Student(models.Model):
    roll_no = models.IntegerField()
    name = models.CharField(max_length=100)
    physics_marks = models.IntegerField()
    chemistry_marks = models.IntegerField()
    maths_marks = models.IntegerField()
    performance = models.FloatField()

    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    
    def save(self, *args, **kwargs):
        # Automatically calculate performance
        self.performance = (self.physics_marks + self.chemistry_marks + self.maths_marks) / 3
        super().save(*args, **kwargs)

class Teacher(models.Model):
    employee_id = models.IntegerField()
    name = models.CharField(max_length=100)
    
    def calculate_performance(self):
        students = Student.objects.filter(teacher=self)
        if students.exists():
            total_performance = sum([student.performance for student in students])
            return total_performance / students.count()
        return 0
```
## API creation for performing different operations 
### views.py
```python

from django.shortcuts import render
from .models import Student, Teacher  # Import Teacher model as well
from .serializer import Student_serializer, Teacher_serializer
from django.db.models import Avg, Q, F, Sum, Count, ExpressionWrapper, FloatField
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class StudentCrudView(APIView):
    # function to post data
    def post(self, request):
        serializer = Student_serializer(data=request.data,many=True)
        
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
            .values('teacher_id')  # Use 'teacher_id' instead of 'class_teacher'
            .annotate(
                passed_students=Count('roll_no'),
                total_students=Count('teacher_id')  # Use 'teacher_id' instead of 'class_teacher'
            )
            .order_by('-passed_students')
        )

        if best_teacher_data.exists():
            best_teacher = best_teacher_data.first()
            teacher = Teacher.objects.get(employee_id=best_teacher['teacher_id'])  # Fetch Teacher instance
            response_data = {
                "best_teacher": teacher.name,  # Get the teacher's name from Teacher model
                "passed_students": best_teacher['passed_students'],
                "total_students": best_teacher['total_students'],
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
            return Response({"error": "Invalid subject"}, status=status.HTTP_400_BAD_REQUEST)

        # Serialize the list of students who failed in the specified subject
        serializer = Student_serializer(failed_students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
