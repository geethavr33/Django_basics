import random
from school.models import School
from department.models import Department  # Adjust the import based on your app structure
 
def assign_random_departments_to_schools(num_departments_to_assign=2):
    schools = School.objects.filter(is_active=True)
    departments = Department.objects.filter(is_active=True)
 
    for school in schools:
        # Randomly select departments to assign
        selected_departments = random.sample(list(departments), k=min(num_departments_to_assign, len(departments)))
 
        # Clear existing department associations
        school.depart_id.clear()
 
        # Add selected departments to the school
        for department in selected_departments:
            school.depart_id.add(department)
 
        print(f"Assigned departments to {school.name}: {[dept.name for dept in selected_departments]}")
 
    print("All active schools have been updated with random departments.")
 
# Entry point for django-extensions
def run():
    assign_random_departments_to_schools()
 
 