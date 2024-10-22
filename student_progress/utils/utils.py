from app_student_progress.models import Student, Teacher
def calculate_teacher_pass_percentage(teacher_id):
    # Count the total number of students for the given teacher
    total_students = Student.objects.filter(teacher_id=teacher_id).count()
   
    # Count passed students for the teacher (total_marks > 150)
    passed_students_count = Student.objects.filter(teacher_id=teacher_id, total_marks__gt=150).count()
 
    if total_students > 0:
        # Calculate pass percentage
        pass_percentage = (passed_students_count / total_students) * 100
        return round(pass_percentage, 2)
   
    return 0