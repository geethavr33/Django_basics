# Student Progress Management System API
## Overview
Here's the API documentation for managing Student progress, including their marks, assigned teachers, departments, and school details. 

## Base URL
```url
http://<your-domain>/
```

## End Points in this project
# API Endpoints
There are 24 endpoints in total for your project. Here’s the breakdown by section:
* School API Endpoints: 6
* Department API Endpoints: 9
* Teacher API Endpoints: 8
* Student API Endpoints: 11


### School API Endpoints

| Endpoint                                        | Method            | Description                                               |
|-------------------------------------------------|-------------------|-----------------------------------------------------------|
| `/schools/`                                  | GET, POST         | Retrieve all schools or create a new school record.       |
| `/schools/<int:pk>/`              | GET, PUT, DELETE  | Retrieve, update, or delete a school by ID.    
|`schools/<int:school_id>/`     |GET            | Get School details           |
| `schools/<int:school_id>/departments/`           | GET               | List departments within a specific school.                |
| `schools/<int:school_id>/teachers/`              | GET               | List teachers within a specific school.                   |
| `schools/<int:school_id>/students/`              | GET               | List students within a specific school.                   |

---

### Department API Endpoints

| Endpoint                                       | Method            | Description                                   |
|------------------------------------------------|-------------------|-----------------------------------------------|
| `/department/`                             | GET, POST         | Retrieve all departments or create a new department. |
| `departments/create,update,delete/`             | GET, PUT, DELETE  | Retrieve, update, or delete a department by ID. |
| `/departments/<int:pk>/`      | GET               | Filter departments by department ID.               |
| `departments/<int:dept_id>/teachers/`     | GET               | Retrieve teachers under a specific department by ID. |
| `departments/<int:dept_id>/students/`     | GET               | Retrieve students under a specific department by ID. |
| `departments/<int:dept_id>/details/`  |    GET    |Retrieve details of department |
| `departments/<int:department_id>/inactivate/`|    PUT | Inactivate Department |
---


### Teacher API Endpoints

| Endpoint                                         | Method            | Description                                               |
|--------------------------------------------------|-------------------|-----------------------------------------------------------|
| `/teachers/`                                 | GET, POST         | Retrieve all teachers          |
| `/teachers/create/`                              |POST                |Create teachers
| `/teachers/<teacher_id>/create,update,delete/`   | GET, PUT, DELETE  | Retrieve, update, or delete a teacher by ID.              |
| `/teachers/<int:teacher_id>/total-students/`     | GET               | Retrieve total students of a specific teacher.           |
| `teacherdetails/<int:teacher_id>/`                 | GET              | Retrieve teacher details.        |
| `teachers/performance/`                   | GET               | Generate a performance report for all teachers and find best teacher .           |
| `teachers/<int:teacher_id>/inactivate/`    | PUT               | Inactivate a  teacher.     |
                   |

---

### Student API Endpoints

| Endpoint                                         | Method            | Description                                               |
|--------------------------------------------------|-------------------|-----------------------------------------------------------|
| `/students/`                                 | GET, POST         | Retrieve all students or create a new student record.     |
| `students/<int:roll_no>/`                    | GET, PUT, DELETE  | Retrieve, update, or delete a student by ID.              |
| `students/subjectwise_failed/`               | GET               | Retrieve students sorted by failed in a specific subject.  |
| `students/toppers/`               | GET               | Retrieve toppers.  |

| `students/above_cutoff/`               | GET               | Retrieve students sorted by above cutoff.  |

| `students/failed/`               | GET               | Retrieve students sorted by failed .  |

| `students/average/`               | GET               | Retrieve students sorted by above or below average.  |

| `students/subjectwise_failed/`               | GET               | Retrieve students sorted by failed in a specific subject.  |

| `students/filter/`            | GET               | Retrieve statistics based on the specified filtration average-marks/, report-failed/, top5/.    |
| `students/<str:class_teacher>/`            | GET               | Retrieve students based on the class teacher.    |
| `students/<int:student_id>/inactivate/`            | PUT               | Inactivate a student.    |


# Student APP
##### Base URL
##### http://127.0.0.1:8000/students/
Student API Endpoints
1. Create a Student
•	Endpoint: /students/
•	Method: POST
•	Description: Creates a new Student entry. The total_marks and percentage fields are automatically calculated upon saving.
Request Body (JSON):
```json
{
    "name": "John Doe",
    "maths_marks": 85.5,
    "chemistry_marks": 78.0,
    "physics_marks": 92.0,
    "teacher_id": 1
}
```
Response (201 Created):
```json
{
    "roll_no": 1,
    "name": "John Doe",
    "maths_marks": 85.5,
    "chemistry_marks": 78.0,
    "physics_marks": 92.0,
    "total_marks": 255.5,
    "percentage": 85.17,
    "teacher_id": 1,
    "created_on": "2024-10-26T12:34:56Z",
    "updated_on": "2024-10-26T12:34:56Z"
}
________________________________________
2. Retrieve a Student by Roll Number
•	Endpoint: /students/<roll_no>/
•	Method: GET
•	Description: Fetches a Student instance by roll_no.
Response (200 OK):
``` json
{
    "roll_no": 1,
    "name": "John Doe",
    "maths_marks": 85.5,
    "chemistry_marks": 78.0,
    "physics_marks": 92.0,
    "total_marks": 255.5,
    "percentage": 85.17,
    "teacher_id": 1,
    "created_on": "2024-10-26T12:34:56Z",
    "updated_on": "2024-10-26T12:34:56Z"
}
```________________________________________
# 3. Update a Student by Roll Number
•	Endpoint: /students/<roll_no>/
•	Method: PUT
•	Description: Updates an existing Student. The fields total_marks and percentage are recalculated upon saving.
Request Body (JSON):
``` json
{
    "name": "Jane Doe",
    "maths_marks": 90.0,
```
________________________________________
# 4. Update a Student by Roll Number (continued)
•	Endpoint: /students/<roll_no>/
•	Method: PUT
•	Description: Updates an existing Student record by their roll number. The fields total_marks and percentage are recalculated upon saving.
Request Body (JSON):
``` json
{
    "name": "Jane Doe",
    "maths_marks": 90.0,
    "chemistry_marks": 85.0,
    "physics_marks": 88.0,
    "teacher_id": 2
}
Response (200 OK):
json
{
    "roll_no": 1,
    "name": "Jane Doe",
    "maths_marks": 90.0,
    "chemistry_marks": 85.0,
    "physics_marks": 88.0,
    "total_marks": 263.0,
    "percentage": 87.67,
    "teacher_id": 2,
    "created_on": "2024-10-26T12:34:56Z",
    "updated_on": "2024-10-26T13:00:56Z"
}
```
________________________________________
## 5. Delete a Student by Roll Number
* Endpoint: /students/<roll_no>/
* Method: DELETE
* Description: Deletes a Student entry by roll_no.
Response (204 No Content):
json
{}
_________________________________________

## 6. StudentFilterBySubjectAndTeacherView
* GET /students/filter/?subject=maths
* Filter students by highest marks in a specified subject.

Parameters:
subject: physics, chemistry, or maths.
#### GET /students/filter/?teacher_id=<teacher_id>
Filter students by the specified teacher.

Response:
#### 200 OK: Returns filtered students based on the criteria.
#### 400 Bad Request: Returns an error if invalid parameters are provided.

## 7. StudentDetailView
### PUT /students/<roll_no>/
Update student details.
### Request Body:
```json
{
    "name": "Updated Name",
    "maths_marks": 80
}
```

## 8. TopperListView
GET /students/topper/
### Retrieve the student with the highest marks.

Response:
#### 200 OK: Returns the topper’s data.
#### 404 Not Found: If no students are found.
### 10. FailedStudentsListView
### GET /students/failed/
Retrieve students who failed in any subject.

Response:
* 200 OK: Returns a list of failed students.
* 400 Bad Request: Returns an error if data retrieval fails.
  
## 9. SubjectWiseFailedListView
* GET /students/failed/subject/?subject=maths
* Retrieve students who failed in a specified subject.

Parameters:
##### subject: physics, chemistry, or maths.
Response:
* 200 OK: Returns a list of failed students for the given subject.
* 400 Bad Request: Returns an error if the subject is invalid or missing.
  
## 10. StudentsAboveCutoffView
GET /students/above_cutoff/?cutoff=150
##### Retrieve students whose total marks exceed a specified cutoff.

Parameters:

cutoff (optional): Total cutoff marks (default is 150).
### Response:

* 200 OK: Returns a list of students above the cutoff.
  
## 11. StudentsAboveAndBelowAverageView
GET /students/average/
* Retrieve students who scored above and below average.

Response:
* 200 OK: Returns a JSON object with average_marks, students_below_average, and students_above_average.


  
## 12.  StudentsPassedInAllSubjectsView
GET /students/passed_all/
### Retrieve students who passed all subjects.

Response:
* 200 OK: Returns a list of students who passed all subjects.
## 13. StudentsFailedInAllSubjectsView
GET /students/failed_all/
#### Retrieve students who failed in all subjects.

Response:
* 200 OK: Returns a list of students who failed all subjects.
  
## 14.  StudentsPassedInSubjectView
GET /students/passed/<subject>/
### Retrieve students who passed in a specific subject.

Path Parameter:

subject: physics, chemistry, or maths.
### Response:

* 200 OK: Returns a list of students who passed in the specified subject.

### 15.StudentsPassedInAtLeastOneSubjectView
GET /students/passed_at_least_one/
### Retrieve students who passed in at least one subject.

Response:
* 200 OK: Returns a list of students who passed at least one subject.


## 16. TopStudentsView

GET /students/top_students/
### Retrieve the top 10 students based on total marks.

Response:
200 OK: Returns a list of the top 10 students.




Models
Student_Progress

| Field           | Type         | Description                                           |
|-----------------|--------------|-------------------------------------------------------|
| `roll_no`       | Integer      | Unique identifier for the student (auto-generated)    |
| `name`          | String       | Name of the student                                   |
| `chemistry_mark`| Float        | Marks in Chemistry (0-100)                            |
| `physics_mark`  | Float        | Marks in Physics (0-100)                              |
| `maths_mark`    | Float        | Marks in Mathematics (0-100)                          |
| `percentage`    | Float        | Percentage score based on total marks                 |
| `cut_off`       | Integer      | Default total marks (300)                             |
| `teacher_id   ` | Foreign Key  | The teacher assigned to the class                     |
| `created_at`    | DateTime     | Timestamp of record creation                          |
| `updated_at`    | DateTime     | Timestamp of last update                              |
| `is_active`     | Boolean      | Active or not                                         |


# TEACHER APP
Teacher API Endpoints
## 1. Create a Teacher
* 	Endpoint: /api/teachers/
* 	Method: POST
* 	Description: Creates a new Teacher entry.
### Request Body (JSON):
```json
{
    "name": "Mr. Smith",
    "performance": 0.0,
    "sc_id": 1,
    "depart_id": 2
}
Response (201 Created):

{
    "emp_id": 1,
    "name": "Mr. Smith",
    "performance": 0.0,
    "sc_id": 1,
    "depart_id": 2,
    "created_on": "2024-10-26T12:34:56Z",
    "updated_on": "2024-10-26T12:34:56Z"
}
```________________________________________
## 2. Retrieve a Teacher by Employee ID
*  Endpoint: /api/teachers/<emp_id>/
* 	Method: GET
*	Description: Fetches a Teacher instance by emp_id.
### Response (200 OK):
```json
Copy code
{
    "emp_id": 1,
    "name": "Mr. Smith",
    "performance": 0.0,
    "sc_id": 1,
    "depart_id": 2,
    "created_on": "2024-10-26T12:34:56Z",
    "updated_on": "2024-10-26T12:34:56Z"
}
```
________________________________________

## 3. Update a Teacher by Employee ID
*	Endpoint: /api/teachers/<emp_id>/
*	Method: PUT
*	Description: Updates an existing Teacher entry by their emp_id.
### Request Body (JSON):
```json
{
    "name": "Mr. Johnson",
    "performance": 85.5,
    "sc_id": 2,
    "depart_id": 3
}
Response (200 OK):

{
    "emp_id": 1,
    "name": "Mr. Johnson",
    "performance": 85.5,
    "sc_id": 2,
    "depart_id": 3,
    "created_on": "2024-10-26T12:34:56Z",
    "updated_on": "2024-10-26T13:01:56Z"
}
```
________________________________________
### 4. Delete a Teacher by Employee ID
*	Endpoint: /api/teachers/<emp_id>/
*	Method: DELETE
*	Description: Deletes a Teacher entry by emp_id.
Response (204 No Content):
json
{}
________________________________________
## 5.API Documentation for SortByTeacher
#### Endpoint: GET /sort-by-teacher/{class_teacher}/
#### Description: Retrieves a list of students assigned to the specified teacher.

Path Parameters:

class_teacher (string): The name of the teacher whose students are to be fetched.
### Responses:

* 200 OK: Successfully retrieved the list of students.

### Response Body:
```json
[
    {
        "name": "Student Name",
        "roll_no": 1,
        "maths_marks": 85,
        "chemistry_marks": 78,
        "physics_marks": 90,
        "total_marks": 253,
        "percentage": 84.33,
        "teacher_id": 1,
        "created_on": "2024-10-28T12:00:00Z",
        "updated_on": "2024-10-28T12:00:00Z"
    },
    ...
]
404 Not Found: If the teacher does not exist.

Response Body:

{
    "error": "Teacher not found"
}

400 Bad Request: For any other errors.

Response Body:

{
    "error": "Error message"
}
```
## 6.API Documentation for BestTeacherView
#### Endpoint: GET /best-teacher/
#### Description: Retrieves the teacher with the highest number of students who passed all subjects.

### Responses:
### 200 OK: Successfully retrieved the best teacher.

Response Body:
```json
{
    "best_teacher": "Teacher Name",
    "passed_students": 20,
    "total_students": 25
}
404 Not Found: If no students are found.

Response Body:

{
    "message": "No students found"
}

Notes
*	All timestamps (created_on and updated_on) are in UTC format.
*	Fields total_marks and percentage for Student are computed automatically upon saving.
*	Only valid emp_id, sc_id, and depart_id values should be provided in Teacher creation and update requests to avoid integrity errors.
* This API documentation provides a comprehensive guide to the CRUD operations on the Student and Teacher models, with the necessary endpoints, methods, and sample request/response formats.



## Teacher Model
| Field           | Type         | Description                                                   |
|-----------------|--------------|---------------------------------------------------------------|
| emp_id      | Integer      | Unique identifier for the teacher (auto-generated)            |
| name            | String       | Name of the teacher                                           |
| depart_id      | Foreign Key  | Department associated with the teacher                        |
| sc_id          | Foreign Key  | School where the teacher is employed                          |
| created_at      | DateTime     | Timestamp of record creation                                  |
| updated_at      | DateTime     | Timestamp of last update                                      |


# Department APP

### Department API Endpoints
### 1. List All Departments
*	Endpoint: /api/departments/
*	Method: GET
*	Description: Retrieves a list of all department entries.
Response (200 OK):
```json
[
    {
        "id": 1,
        "name": "Computer Science",
        "hod": 3,
        "school_id": 1,
        "created_on": "2024-10-26T12:34:56Z",
        "updated_on": "2024-10-26T12:34:56Z"
    },
    {
        "id": 2,
        "name": "Mathematics",
        "hod": 4,
        "school_id": 2,
        "created_on": "2024-10-26T12:35:56Z",
        "updated_on": "2024-10-26T12:35:56Z"
    }
]
```
________________________________________
## 2. Create New Department(s)
*	Endpoint: /api/departments/create/
*	Method: POST
*	Description: Creates one or more new department entries.
Request Body (JSON):
```json
[
    {
        "name": "Physics",
        "hod": 5,
        "school_id": 3
    },
    {
        "name": "Biology",
        "hod": 6,
        "school_id": 4
    }
]
Response (201 Created):

[
    {
        "id": 3,
        "name": "Physics",
        "hod": 5,
        "school_id": 3,
        "created_on": "2024-10-26T13:00:00Z",
        "updated_on": "2024-10-26T13:00:00Z"
    },
    {
        "id": 4,
        "name": "Biology",
        "hod": 6,
        "school_id": 4,
        "created_on": "2024-10-26T13:00:00Z",
        "updated_on": "2024-10-26T13:00:00Z"
    }
]
Error Response (400 Bad Request):

{
    "error": "Invalid data input"
}
```________________________________________
## 3. Retrieve Department by ID
*	Endpoint: /api/departments/<id>/
*	Method: GET
*	Description: Retrieves details of a specific department by its ID.
### Response (200 OK):
```json
{
    "id": 1,
    "name": "Computer Science",
    "hod": 3,
    "school_id": 1,
    "created_on": "2024-10-26T12:34:56Z",
    "updated_on": "2024-10-26T12:34:56Z"
}
Error Response (404 Not Found):
{
    "error": "Department not found"
}
```________________________________________
## 4. Update Department by ID
*	Endpoint: /api/departments/<id>/
*	Method: PUT
*	Description: Updates details of a specific department by its ID. Only the fields provided in the request body will be updated.
### Request Body (JSON):
```json
{
    "name": "Mathematics and Computing",
    "hod": 7
}
Response (200 OK):

{
    "id": 1,
    "name": "Mathematics and Computing",
    "hod": 7,
    "school_id": 1,
    "created_on": "2024-10-26T12:34:56Z",
    "updated_on": "2024-10-26T13:30:56Z"
}
Error Response (404 Not Found):

{
    "error": "Department not found"
}
Error Response (400 Bad Request):

{
    "error": "Invalid data input"
}
```________________________________________
## 5. Delete Department by ID
*	Endpoint: /api/departments/<id>/
*	Method: DELETE
*	Description: Deletes a specific department by its ID.
### Response (204 No Content):
```json
{}
Error Response (404 Not Found):

{
    "error": "Department not found"
}
________________________________________
Notes
•	hod refers to the ID of the Head of Department (foreign key).
•	school_id refers to the associated school’s ID (foreign key).
•	In update requests, only fields needing change need to be provided in the body.
This documentation provides comprehensive details on all the CRUD operations available for Department using the respective endpoints, methods, request/response formats, and error handling.






## Department Model
| Field           | Type         | Description                                         |
|-----------------|--------------|-----------------------------------------------------|
| dept_id   | Integer      | Unique identifier for the department (primary key)  |
|  name       String       | Name of the department                              |
| hod        | String       | Name of the Head of Department (HOD) (unique)       |
| sc_id          | Foreign Key  | Reference to the school the department belongs to   |
| created_at      | DateTime     | Timestamp of record creation                        |
| updated_at      | DateTime     | Timestamp of last update                            |

# School APP
# School API Endpoints
### 1. List All Schools
*	Endpoint: /schools/
*	Method: GET
*	Description: Retrieves a list of all schools in the database.
### Response (200 OK):
```json
[
    {
        "school_id": 1,
        "name": "Greenwood High",
        "location": "Greenwood City",
        "created_on": "2024-10-26T12:00:00Z",
        "updated_on": "2024-10-26T12:00:00Z"
    },
    {
        "school_id": 2,
        "name": "Oakridge International",
        "location": "Oakville",
        "created_on": "2024-10-26T12:05:00Z",
        "updated_on": "2024-10-26T12:05:00Z"
    }
]
```
_______________________________________
### 2. Create New School
*	Endpoint: /schools/
*	Method: POST
*	Description: Creates a new school entry.
#### Request Body (JSON):
```json
{
    "name": "Pine Valley School",
    "location": "Pine Valley"
}
Response (201 Created):

{
    "school_id": 3,
    "name": "Pine Valley School",
    "location": "Pine Valley",
    "created_on": "2024-10-26T12:30:00Z",
    "updated_on": "2024-10-26T12:30:00Z"
}
Error Response (400 Bad Request):

{
    "name": [
        "This field is required."
    ],
    "location": [
        "This field is required."
    ]
}
```
________________________________________
### 3. Retrieve School by ID
*	Endpoint: /schools/<school_id>/
*	Method: GET
*	Description: Retrieves details of a specific school by its ID.
### Response (200 OK):
```json
{
    "school_id": 1,
    "name": "Greenwood High",
    "location": "Greenwood City",
    "created_on": "2024-10-26T12:00:00Z",
    "updated_on": "2024-10-26T12:00:00Z"
}
Error Response (404 Not Found):

{
    "error": "School not found."
}
```
________________________________________
### 4. Update School by ID
*	Endpoint: /schools/<school_id>/
*	Method: PUT
*	Description: Updates details of a specific school by its ID.
#### Request Body (JSON):
```json
{
    "name": "Greenwood International",
    "location": "Greenwood Town"
}
Response (200 OK):

{
    "school_id": 1,
    "name": "Greenwood International",
    "location": "Greenwood Town",
    "created_on": "2024-10-26T12:00:00Z",
    "updated_on": "2024-10-26T13:00:00Z"
}
Error Response (404 Not Found):

{
    "error": "School not found."
}
Error Response (400 Bad Request):

{
    "error": "Invalid data input"
}
```
________________________________________
### 5. Delete School by ID
*	Endpoint: /schools/<school_id>/
*	Method: DELETE
*	Description: Deletes a specific school by its ID.
Response (204 No Content):
```json
{}
Error Response (404 Not Found):

{
    "error": "School not found."
}
```
________________________________________
Notes
*	school_id: Unique identifier for each school.
*	Only fields that need updating are required in the body for PUT requests.
This documentation provides a comprehensive overview of the CRUD operations available for the School model, including the necessary endpoints, methods, request and response formats, and error handling.


## Model
### School Model Fields

| Field         | Type      | Description                                    |
|---------------|-----------|------------------------------------------------|
| `school_id`   | Integer   | Unique identifier for each school (primary key). |
| `name`        | String    | Name of the school.                            |
| `location`     | String    | location of the school.                         |
| `created_at`  | DateTime  | Timestamp of record creation.                  |
| `updated_at`  | DateTime  | Timestamp of last update.  

