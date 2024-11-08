
from django.utils import timezone
import random
from django.contrib.auth.hashers import make_password  # Correct way to hash passwords
from app_teacher.models import Teacher
from userapp_new.models import UserNew
 
def make_teacher_as_user():
    # Filter Active Teachers
    teachers = Teacher.objects.filter(is_active=True)
    role = ["Teacher", "Principal", "Staff"]
   
    # Loop Through Each Active Teacher
    for teacher in teachers:
        # Generate Username:
        username = f"{teacher.name.lower()}"
        plain_password = f"{username}123"
        print("Password is:", plain_password)
       
        # Hash the password
        hashed_password = make_password(plain_password)  # Hash the password properly
 
        # Check If Username Already Exists
        if UserNew.objects.filter(username=username).exists():
            print(f"Username '{username}' already exists for another CustomUser")
            continue
 
        # Extract first and last name from the teacher name
        first_name, last_name = teacher.name.split()[0], teacher.name.split()[1] if len(teacher.name.split()) > 1 else ""
       
        # If the username does not already exist, create a new user instance
        user = UserNew(
            employee_id=teacher.emp_id,  # Make sure this matches field name
            username=username,
            password=hashed_password,
            last_login=timezone.now(),  # Corrected this line
            performance=teacher.performance,
            first_name=first_name,
            last_name=last_name,
            school_ID=teacher.sc_id,
            is_active=teacher.is_active,
            created_on=teacher.created_on,
            updated_on=teacher.updated_on,
        )
        user.save()  # Save the user
 
        # Set Many-to-Many Relationships
        user.department_ID.set(teacher.dept_id.all())  # Set the departments for the user
 
        print(f"Created user: {user.username} with a generated password, performance: {user.performance}, "
              f"school ID: {user.school_ID}, departments: {list(user.department_ID.all())}")
 
 
def run():
    make_teacher_as_user()