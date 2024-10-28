# API Documentation

Here's the API documentation for managing Student model based on the structure provided. The documentation includes endpoints for creating, retrieving, updating, and deleting records.
________________________________________
## API Documentation for Student  Model
________________________________________
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
## 8.Delete a student by roll number.
DELETE /students/<roll_no>/

Response:
#### 204 No Content: Student successfully deleted.
#### 404 Not Found: If student does not exist.

## 9. TopperListView
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
  
## 11. SubjectWiseFailedListView
* GET /students/failed/subject/?subject=maths
* Retrieve students who failed in a specified subject.

Parameters:
##### subject: physics, chemistry, or maths.
Response:
* 200 OK: Returns a list of failed students for the given subject.
* 400 Bad Request: Returns an error if the subject is invalid or missing.
  
## 12. StudentsAboveCutoffView
GET /students/above_cutoff/?cutoff=150
##### Retrieve students whose total marks exceed a specified cutoff.

Parameters:

cutoff (optional): Total cutoff marks (default is 150).
### Response:

* 200 OK: Returns a list of students above the cutoff.
  
## 13. StudentsAboveAndBelowAverageView
GET /students/average/
* Retrieve students who scored above and below average.

Response:
* 200 OK: Returns a JSON object with average_marks, students_below_average, and students_above_average.

## 14. StudentsFailedInSubjectView

GET /students/failed/<subject>/
##### Retrieve students who failed in a specific subject.

Path Parameter:

subject: physics, chemistry, or maths.
Response:

* 200 OK: Returns a list of failed students for the specified subject.
* 400 Bad Request: Returns an error if the subject is invalid.
  
## 15.  StudentsPassedInAllSubjectsView
GET /students/passed_all/
### Retrieve students who passed all subjects.

Response:
* 200 OK: Returns a list of students who passed all subjects.
## 16. StudentsFailedInAllSubjectsView
GET /students/failed_all/
#### Retrieve students who failed in all subjects.

Response:
* 200 OK: Returns a list of students who failed all subjects.
  
## 17.  StudentsPassedInSubjectView
GET /students/passed/<subject>/
### Retrieve students who passed in a specific subject.

Path Parameter:

subject: physics, chemistry, or maths.
### Response:

* 200 OK: Returns a list of students who passed in the specified subject.

### 18.StudentsPassedInAtLeastOneSubjectView
GET /students/passed_at_least_one/
### Retrieve students who passed in at least one subject.

Response:
* 200 OK: Returns a list of students who passed at least one subject.

## 19. StudentsFailedInAtLeastOneSubjectView
GET /students/failed_at_least_one/
### Retrieve students who failed in at least one subject.

Response:
* 200 OK: Returns a list of students who failed in at least one subject.
  
## 20. TopStudentsView

GET /students/top_students/
### Retrieve the top 10 students based on total marks.

Response:
200 OK: Returns a list of the top 10 students.





