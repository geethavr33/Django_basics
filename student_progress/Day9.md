# Adding New API

```python

class TopperListView(APIView):
    def get(self, request):
        # Get the topper(s) with the highest total marks
        topper = Student.objects.order_by('-physics_marks', '-chemistry_marks', '-maths_marks').first()
        if topper:
            serializer = Student_serializer(topper)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"message": "No students found"}, status=status.HTTP_404_NOT_FOUND)
class TopStudentsView(APIView):
    def get(self, request):
        # Calculate total marks for each student
        students = Student.objects.annotate(
            total_marks=F('physics_marks') + F('chemistry_marks') + F('maths_marks')
        ).order_by('-total_marks')[:10]  # Order by total marks and take the top 10

        # Serialize and return the student data
        top_students = students.values('roll_no', 'name', 'physics_marks', 'chemistry_marks', 'maths_marks', 'total_marks')
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
        
class GetTeacherDetails(APIView):
    def get(self,request,teacher_id):
        try:
            teacher=Teacher.objects.get(emp_id=teacher_id)
            serializer=Teacher_serializer(teacher)
            return Response({'Teacher':serializer.data},status=status.HTTP_200_OK)

        except Teacher.DoesNotExist:
           return Response({'error':'Teacher not found'},status=status.HTTP_404_NOT_FOUND)
```
 
```