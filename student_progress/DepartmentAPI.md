# API documentation for the Department views:
________________________________________
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




