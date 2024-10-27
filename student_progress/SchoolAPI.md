
# School API Endpoints
### 1. List All Schools
*	Endpoint: /api/schools/
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
*	Endpoint: /api/schools/
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
*	Endpoint: /api/schools/<school_id>/
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
*	Endpoint: /api/schools/<school_id>/
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
*	Endpoint: /api/schools/<school_id>/
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
