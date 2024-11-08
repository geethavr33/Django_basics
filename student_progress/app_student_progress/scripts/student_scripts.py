
import random
from app_student_progress.models import Student
from school.models import School
from app_teacher.models import Teacher

def update_students_schools():
    active_schools = School.objects.filter(is_active=True)
 
 
    if not active_schools:
        print("No active schools found. Aborting update.")
        return
   
    for student in Student.objects.all():
 
        random_school = random.choice(active_schools)
        student.sc_id = random_school
        student.save()
        print(f"Updated student {student.name} with school {random_school.name}")
    print('All students have been updated with random school IDs.')
 
 
def assign_departments_to_students():
    students = Student.objects.all()  # Retrieve all students
    for student in students:
        school = student.sc_id  # Get the school associated with the student
       
        if school:  # Check if the school exists
            print(f"School: {school.sc_id}")  # Print the school name
           
            # Fetch departments associated with the school
            departments = school.depart_id.all()  # Assuming department_ID is a related name for departments
 
            if departments.exists():  # Check if there are any departments
                
                selected_department = random.choice(departments)  # Randomly select one department
               
                # Assign the selected department to the student
                student.dept_id = selected_department  # Assign the ForeignKey
                student.save()  # Save the updated student
               
                print(f"Assigned department {selected_department.dept_id} to student {student.roll_no} in school {school.sc_id}")
            else:
                print(f"No departments found for school {school.name}")
        else:
            print(f"Student {student.name} has no associated school.")
 
def assign_teacher_to_students():
    students = Student.objects.all()  # Get all students
    for student in students:
        department = student.dept_id  # Get the single department for the student
        school = student.sc_id  # Get the single school for the student
        if department and school:  # Ensure the student has a department
            # Find teachers associated with the student's department
            teachers = Teacher.objects.filter(dept_id=department, sc_id=school)
            for teacher in teachers:
                print(f"Teacher: {teacher.emp_id}")  # Print the teacher's nam
 
            if teachers.exists():
                selected_teacher = teachers.first()  # Choose the first teacher for simplicity
                print(selected_teacher.emp_id)
                student.teacher_id = selected_teacher  # Assign the teacher to the student
                student.save()  # Save the updated student
 
                print(f"Assigned teacher {selected_teacher.name} to student {student.name} in department {department.name}")
            else:
                print(f"No teachers found for department {department.name}")
        else:
            print(f"Student {student.name} has no associated department")
 

def run():

    assign_teacher_to_students()
 
 
 
