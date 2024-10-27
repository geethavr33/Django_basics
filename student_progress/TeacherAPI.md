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

