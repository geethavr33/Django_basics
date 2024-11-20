
# Matrimonial Website API Documentation

## Introduction

This document provides detailed information on the API endpoints for the Matrimonial Website. It includes endpoints for managing users, profiles, preferences, matches, subscriptions, messages, notifications, and master codes. Each section describes the functionality, request parameters, and responses for the respective API.

---
**Base URL**: (http://127.0.0.1:8000/api/)
---
## End Points in this project
###### There are 20 endpoints in total for your project. Here’s the breakdown by section:

* **User API Endpoints: 4**
* **Profile API Endpoints: 2**
* **Preferences API Endpoints: 2**
* **Matching API Endpoints: 1**
* **Subscription API Endpoints: 1**
* **Message API Endpoints: 3**
* **Notification API Endpoints: 5**
* **MasterCode API Endpoints: 2**

### User API Endpoints


| Endpoint                                        | Method            | Description                                               |
|-------------------------------------------------|-------------------|-----------------------------------------------------------|
| `/api/user/create/`                                  | POST         |  create a new User record.       |
| `/api/user/`                                             |GET         |Retrive all users          |
| `/api/users/<user_id>/`              | GET, PUT, DELETE  | Retrieve, update, or delete a user by ID.               |
| `/api/login/`           | GET               | Login with username and password to create JWT Token      |


### Profile API Endpoints


| Endpoint                                        | Method            | Description                                               |
|-------------------------------------------------|-------------------|-----------------------------------------------------------|
| `/api/profiles/`                                  | GET, POST         | Retrieve all Users or create a new User profile.       |
| `/api/profiles/<profile_id>/`              | GET, PUT, DELETE  | Retrieve, update, or delete a User by ID.               |


### Preferences API Endpoints


| Endpoint                                        | Method            | Description                                               |
|-------------------------------------------------|-------------------|-----------------------------------------------------------|
| `/api/preferences/`                                  | GET, POST         | Retrieve all preferences or create a new preferences .       |
| `/api/preferences/<preference_id>/`              | GET, PUT, DELETE  | Retrieve, update, or delete a preference by ID.               |

### Matching API Endpoints


| Endpoint                                        | Method            | Description                                               |
|-------------------------------------------------|-------------------|-----------------------------------------------------------|
| `/api/match/`                                  |  POST         | Retrieve matches for a specific user.
          |
### Subscription API Endpoints

| Endpoint                                        | Method            | Description                                               |
|-------------------------------------------------|-------------------|-----------------------------------------------------------|
| `/api/subscriptions/`                            | GET, POST         | Retrieve all subscriptions or create a new subscription.|
      |
### Message API Endpoints

| Endpoint                                        | Method            | Description                                               |
|-------------------------------------------------|-------------------|-----------------------------------------------------------|
| `/api/send-match-messages/`                 | POST  | send  messages by matching table id if match occurs             |
| `/send-matching-message/`              | POST  | send  messages by user id if match occurs
| `/api/get-read-message/<user_id>/`           | GET               | Retrieve all messages for a specific user.  |
             |

### Notification API Endpoints

| Endpoint                                        | Method            | Description                                               |
|-------------------------------------------------|-------------------|-----------------------------------------------------------|
| `/notifications/incomplete-profile/<int:user_id>/`                                  | GET        | Send messages to inform incomplete profile/preference       |
| `/api/notifications/festival/`              | GET  | Send bulk notifications regarding festival |
| `/notifications/unread-messages/<int:user_id>/`           | GET               | Send notifications informing about unread messages        |
| `notifications/unread/<int:user_id>/`              | GET               | Send notifications informing about unread notifications        |
| `notifications/<int:user_id>/`              | GET               | List notifications  by user id and change status to Read.                   |

### MasterCode API Endpoints

| Endpoint                                        | Method            | Description                                               |
|-------------------------------------------------|-------------------|-----------------------------------------------------------|
| `/api/mastercodes/`                                  | GET, POST         | Retrieve all master codes or create a new code.   |
| `/mastercodes/<int:pk>/`              | GET, PUT, DELETE  | Retrieve, update, or delete a mastercode by ID.               |


## Authentication


### Authentication Header

Most endpoints require authentication via a token. Include the following header in your requests:


---

## 1. User API

### Endpoints:

#### **1.1 Create User**
- **POST** `/users/create/`

**Request Body**:
```json
{
    "username":"devika",
    "email": "devika@gmail.com",
    "password": "xyz123",
    "first_name": "devika",
    "last_name": "kumar",
    "phone_no": "2114561190",
    "role": "Admin",
    "subscription_plan": "Basic",
    "status": "Active"
}
## Response:
{
  "message": "User registered successfully.",
  "user_id": 1
}
#### **1.2 Login**
POST /users/login/
Request Body:
{
  "username": "devika",
  "password": "xyz123"
}
Response:

json
{
  "token": "JWT_TOKEN"
}

8888888888888888888888888888888888888888888888888888888888888888888888888888888
1.3 Update User
PUT /users/update/{user_id}/
Request Body:

json
Copy code
{
  "first_name": "John",
  "last_name": "Smith",
  "phone_no": "0987654321",
  "email": "johnsmith@example.com"
}
Response:

json
Copy code
{
  "message": "User updated successfully."
}
1.4 Delete User
DELETE /users/delete/{user_id}/
Response:

json
Copy code
{
  "message": "User deleted successfully."
}
2. Profile API
Endpoints:
2.1 Create Profile
POST /profiles/create/
Request Body:

json
Copy code
{
  "user_id": 1,
  "age": 30,
  "bio": "Looking for a partner.",
  "weight": 70,
  "height": 175,
  "religion": "Hindu",
  "caste": "Brahmin",
  "profession": "Engineer",
  "language": "English",
  "education": "Bachelor's",
  "address": "123 Street, City",
  "income": 50000,
  "marital_status": "Single",
  "gender": "Male",
  "date_of_birth": "1994-01-01"
}
Response:

json
Copy code
{
  "message": "Profile created successfully.",
  "profile_id": 1
}
2.2 Update Profile
PUT /profiles/update/{profile_id}/
Request Body:

json
Copy code
{
  "bio": "Looking for a life partner.",
  "weight": 72,
  "height": 177
}
Response:

json
Copy code
{
  "message": "Profile updated successfully."
}
2.3 Delete Profile
DELETE /profiles/delete/{profile_id}/
Response:

json
Copy code
{
  "message": "Profile deleted successfully."
}
3. Preferences API
Endpoints:
3.1 Create Preferences
POST /preferences/create/
Request Body:

json
Copy code
{
  "user_id": 1,
  "age": 28,
  "profession": "Doctor",
  "caste": "Brahmin",
  "education": "Master's",
  "location": "City",
  "height": 170,
  "weight": 65,
  "income": 60000,
  "religion": "Hindu",
  "gender": "Female"
}
Response:

json
Copy code
{
  "message": "Preferences created successfully.",
  "preferences_id": 1
}
3.2 Update Preferences
PUT /preferences/update/{preferences_id}/
Request Body:

json
Copy code
{
  "income": 65000
}
Response:

json
Copy code
{
  "message": "Preferences updated successfully."
}
3.3 Delete Preferences
DELETE /preferences/delete/{preferences_id}/
Response:

json
Copy code
{
  "message": "Preferences deleted successfully."
}
4. Matching API
Endpoints:
4.1 Create Match
POST /matching/create/
Request Body:

json
Copy code
{
  "user1_id": 1,
  "user2_id": 2,
  "match_score": 80
}
Response:

json
Copy code
{
  "message": "Match created successfully.",
  "match_id": 1
}
4.2 Update Match Score
PUT /matching/update/{match_id}/
Request Body:

json
Copy code
{
  "match_score": 85
}
Response:

json
Copy code
{
  "message": "Match score updated successfully."
}
4.3 Delete Match
DELETE /matching/delete/{match_id}/
Response:

json
Copy code
{
  "message": "Match deleted successfully."
}
5. Subscription API
Endpoints:
5.1 Create Subscription
POST /subscriptions/create/
Request Body:

json
Copy code
{
  "user_id": 1,
  "plan_type": "Premium",
  "start_date": "2024-01-01",
  "end_date": "2025-01-01"
}
Response:

json
Copy code
{
  "message": "Subscription created successfully.",
  "subscription_id": 1
}
5.2 Update Subscription
PUT /subscriptions/update/{subscription_id}/
Request Body:

json
Copy code
{
  "plan_type": "Standard"
}
Response:

json
Copy code
{
  "message": "Subscription updated successfully."
}
5.3 Delete Subscription
DELETE /subscriptions/delete/{subscription_id}/
Response:

json
Copy code
{
  "message": "Subscription deleted successfully."
}
6. Message API
Endpoints:
6.1 Send Message
POST /messages/send/
Request Body:

json
Copy code
{
  "sender_id": 1,
  "receiver_id": 2,
  "message_text": "Hello! How are you?"
}
Response:

json
Copy code
{
  "message": "Message sent successfully.",
  "message_id": 1
}
6.2 Update Message
PUT /messages/update/{message_id}/
Request Body:

json
Copy code
{
  "message_text": "Updated message text."
}
Response:

json
Copy code
{
  "message": "Message updated successfully."
}
6.3 Delete Message
DELETE /messages/delete/{message_id}/
Response:

json
Copy code
{
  "message": "Message deleted successfully."
}
7. Notification API
Endpoints:
7.1 Send Notification
POST /notifications/send/
Request Body:

json
Copy code
{
  "user_id": 1,
  "notification_type": "Match",
  "message": "You have a new match!"
}
Response:

json
Copy code
{
  "message": "Notification sent successfully.",
  "notification_id": 1
}
7.2 Update Notification
PUT /notifications/update/{notification_id}/
Request Body:

json
Copy code
{
  "status": "Read"
}
Response:

json
Copy code
{
  "message": "Notification updated successfully."
}
7.3 Delete Notification
DELETE /notifications/delete/{notification_id}/
Response:

json
Copy code
{
  "message": "Notification deleted successfully."
}
8. Master Code API
Endpoints:
8.1 Create Master Code
POST /mastercodes/create/
Request Body:

json
Copy code
{
  "type": "Religion",
  "code": "Hindu",
  "name": "Hindu",
  "display_text": "Hindu"
}
Response:

json
Copy code
{
  "message": "Master code created successfully.",
  "master_code_id": 1
}
8.2 Update Master Code
PUT /mastercodes/update/{master_code_id}/
Request Body:

json
Copy code
{
  "display_text": "Hinduism"
}
Response:

json
Copy code
{
  "message": "Master code updated successfully."
}
8.3 Delete Master Code
DELETE /mastercodes/delete/{master_code_id}/
Response:

json
Copy code
{
  "message": "Master code deleted successfully."
}
Conclusion
This API documentation provides an overview of all
