from app_student_progress.models import Student, Teacher

def calculate_teacher_performance(teacher):
    # Get all students taught by the given teacher
    students = Student.objects.filter(teacher_id=teacher)
    
    # Calculate average performance
    if students.exists():
        total_performance = sum(student.percentage for student in students)
        average_performance = total_performance / students.count()
        return average_performance
    return 0

def run():
    # Display the average performance of all teachers
    teachers = Teacher.objects.all()
    for teacher in teachers:
        avg_performance = calculate_teacher_performance(teacher)
        print(f'Teacher: {teacher.name}, Average Performance: {avg_performance:.2f}')

# Call the run function to execute
if __name__ == "__main__":
    run()
