
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


| Endpoint                   | Method       | Description             |
|----------------------------|--------------|------------------------|
| `/api/user/create/`        | POST         |  create a new User record.                 |
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

# 1.User App
## Authentication


### Authentication Header

Most endpoints require authentication via a token. Include the following header in your requests:


---


## **1.1 Create User**
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
```
* Response:
    - Status 201: Created User
    - Status 400: Validation error or missing required fields.
```json
{
  "message": "User registered successfully.",
  "user_id": 1
}
```
## **1.2 Login**
* POST /users/login/
* Request Body:
```json
{
  "username": "devika",
  "password": "xyz123"
}
```
Response:
    - Status 200: Token generated
    - Status 401: Invalid Credentials.

```json
{
  "token": "JWT_TOKEN"
}
```
## 1.3 Retrive ALL Users
* GET/admin/user/
* Response:

```json
 {
        "id": 1,
        "username": "geetha",
        "email": "geetha@example.com",
        "first_name": "geetha",
        "last_name": "rajan",
        "phone_no": "1234567890",
        "joined_date": "2024-11-12",
        "status": "Active",
        "created_on": "2024-11-12T04:31:45.092594Z",
        "updated_on": "2024-11-19T09:52:53.442736Z",
        "last_login": null,
        "is_active": true,
        "is_admin": true,
        "role": "Normal User"
 }
```
## 1.4 Retrive User by ID
* GET /api/user/{user_id}/
* Response:
   Status 200: Returns User with specific id.
```json
{
    "id": 1,
    "username": "geetha",
    "email": "geetha@example.com",
    "first_name": "geetha",
    "last_name": "rajan",
    "phone_no": "1234567890",
    "joined_date": "2024-11-12",
    "status": "Active",
    "created_on": "2024-11-12T04:31:45.092594Z",
    "updated_on": "2024-11-19T09:52:53.442736Z",
    "last_login": null,
    "is_active": true,
    "is_admin": true,
    "role": "Normal User"
}
```
## 1.5 Update User
* PUT /users/{user_id}/
* Request Body:

```json

 {
    "username": "geetha",
    "email": "geetha@example.com",
    "password": "xyz123",
    "first_name": "geetha",
    "last_name": "rajan",
    "phone_no": "1234567890",
    "role": "Normal User",
    "subscription_plan": "Basic",
    "status": "Active",
    "is_admin":"True"
}
```
* Response:

    - Status 200: Updated student data.
    - Status 400: Validation error or missing required fields.
```json
{
  "message": "User updated successfully."
}
```
## 1.6 Delete User
* DELETE /user/{user_id}/
* Response:
Status 204: No content, successful deletion.

```json
{
  "message": "User deleted successfully."
}
```

### Models
#### User
| Field           | Type         | Description                                           |
|-----------------|--------------|-------------------------------------------------------|
| `id`            | Integer      | Unique identifier for the user (auto-generated)    |
| `username`      | String       | Name of the user                                   |
| `email`         | EmailField   | Email of user                                      |
| `password`      | String       | Password of user                                   |
| `first_name`    | String       | first name of user                                 |
| `last_name`     | String       | last name of user                                  |
| `phone_no`      | String       | Phone number of user                               |
| `status`        | String       | Current status of user                             |
| `role`          | String       | Role of the user(Normal user/Admin)                |
| `joined_date`   | DateField    | Joined date                                        |
| `last_login`    | DateTime     | Last login  date                                   |
| `is_active`     |  Boolean     | User Active or not                                 |
| `is_admin`      |  Boolean     | User Admin or not (Default-False)                  |
| `created_on`    | DateTime     | Timestamp of record creation                       |
| `updated_on`    | DateTime     | Timestamp of last update                           |



# 2.Profile App
## Endpoints:
## 2.1 Create Profile
* POST /profiles/
* Request Body:

```json
{
        "age": 25,
        "bio": "Software developer with 10 years of experience.",
        "weight": 76.0,
        "height": 179.0,
        "language": "Malayalam",
        "address": "Soumya,pathanamthitta",
        "created_on": "2024-11-12T10:45:08.394160Z",
        "updated_on": "2024-11-12T10:50:46.922972Z",
        "image": "/media/profile_images/pexels-italo-melo-2379005_KIHNKPj.jpg",
        "marital_status": "single",
        "status": "Active",
        "family_details": "Living with parents",
        "date_of_birth": "1999-11-25",
        "deactivate": false,
        "user": 1,
        "religion": 1,# hindu
        "caste": 13, # Brahmin
        "education": 6,# Master
        "gender": 30,# Female
        "income": 10,# Medium
        "profession": 25 # Engineer
   
}
```

* Response:
    - Status 201: Created student record.
    - Status 400: Validation error or missing required fields.

## 2.2 Update Profile
* PUT /profiles/{profile_id}/
* Request Body:

```json
{
    "id": 6,
    "age": 25,
    "bio": "Teacherwith 5 years of experience.",
    "weight": 59.0,
    "height": 161.0,
    "language": "Malayalam",
    "address": "pta",
    "created_on": "2024-11-14T09:26:16.385171Z",
    "updated_on": "2024-11-20T05:42:02.599697Z",
    "image": "/media/profile_images/pexels-italo-melo-2379005_FzwSdqJ.jpg",
    "marital_status": "single",
    "status": "Active",
    "family_details": "Living with parents",
    "date_of_birth": "1996-11-25",
    "deactivate": false,
    "user": 6,
    "religion": 1,
    "caste": 13,
    "education": 5,
    "gender": 30,
    "income": 10,
    "profession": 27
}
```
* Response:
    - Status 201: Created student record.
    - Status 400: Validation error or missing required fields.


## 2.3 Delete Profile
* DELETE /profiles/delete/{profile_id}/
* Response:
  - Status 204: No content, successful deletion.
  
### Models
#### Profile

| Field           | Type         | Description                                           |
|-----------------|--------------|-------------------------------------------------------|
| `id`            | Integer      | Unique identifier for the user (auto-generated)    |
| `user    `      | OneToOne     | ID of the user                                     |
| `age  `         | Integer (+)  | age of user                                        |
| `bio     `      | Text         | Bio of user                                        |
| `weight`        | Float        | weight of user                                     |
| `height`        | Float        | height of user                                     |
| `religion`      | ForeignKey   | Religion code from mastercode                      |
| `caste`         | ForeignKey   | caste code from mastercode                         |
| `education`     | ForeignKey   | Education code from mastercode                     |
| `gender`        | ForeignKey   | Gender code from mastercode                        |
| `income`        | ForeignKey   | Income code from mastercode                        |
| `profession`    | ForeignKey   | Profession code from mastercode                    |
| `language`      | String       | language of user                                   |
| `address`       | Text         | Address of user                                    |
| `image`         | ImageField   | Image of user                                      |
| `marital_status`| String       | Marital status of user                             |
| `status`        | String       | Current status of user                             |
| `family_details`| Text         | Family details of user                             |
| `date_of_birth` | DateField    |  date of birth                                     |
| `deactivate`    |  Boolean     | Deactivate user                                    |
| `created_on`    | DateTime     | Timestamp of record creation                       |
| `updated_on`    | DateTime     | Timestamp of last update                           |



# 3. Preferences APP
## Endpoints:
## 3.1 Create Preferences
* POST /preferences/
* Request Body:

```json
{
    "user": 11,
    "age": "24-33",
    "profession": 25,
    "caste": 13,
    "education": 6,
    "location": "India,Us,Uk,USA,Australia",
    "height": 161.0,
    "weight": 59.0,
    "income": 10,
    "religion":1,
    "gender": 29
}
```
* Response:
    - Status 201: Created student record.
    - Status 400: Validation error or missing required fields.
  
## 3.2 Update Preferences
* PUT /preferences/{preferences_id}/
* Request Body:

```json
{
        "id": 1,
        "age": "22-29",
        "location": "India,Us,Uk,USA,Australia",
        "height": 175.0,
        "weight": 70.0,
        "created_on": "2024-11-12T10:57:48.945998Z",
        "updated_on": "2024-11-12T10:57:48.946668Z",
        "user": 2,
        "caste": 13,
        "education": 6,
        "gender": 30,
        "income": 10,
        "profession": 25,
        "religion": 1
}
  ```
* Response:

    - Status 200: Updated User preferences data.
    - Status 400: Validation error or missing required fields.

## 3.3 Delete Preferences
* DELETE /preferences/{preferences_id}/
* Response:
    - Status 204: No content, successful deletion.
   
### Models
#### Preference


| Field           | Type         | Description                                           |
|-----------------|--------------|-------------------------------------------------------|
| `id`            | Integer      | Unique identifier for the user (auto-generated)    |
| `user    `      | OneToOne     | ID of the user                                     |
| `age  `         | Integer (+)  | age of user                                        |
| `weight`        | Float        | weight of user                                     |
| `height`        | Float        | height of user                                     |
| `religion`      | ForeignKey   | Religion code from mastercode                      |
| `caste`         | ForeignKey   | caste code from mastercode                         |
| `education`     | ForeignKey   | Education code from mastercode                     |
| `gender`        | ForeignKey   | Gender code from mastercode                        |
| `income`        | ForeignKey   | Income code from mastercode                        |
| `profession`    | ForeignKey   | Profession code from mastercode                    |
| `location`      | String       | location of user                                   |
| `created_on`    | DateTime     | Timestamp of record creation                       |
| `updated_on`    | DateTime     | Timestamp of last update                           |



# 4.Matching APP
## Endpoints:
##  4.1 Create Match
* POST /match/
* Request Body:

```json
{
  "user_ids":[10]
}
```
* Response:
    - Status 200: Match found succesfully.
    - Status 404: Bad Request.
    - Status 400: Validation error or missing required fields.

### Models
#### Matching

| Field           | Type         | Description                                           |
|-----------------|--------------|-------------------------------------------------------|
| `id`            | Integer      | Unique identifier for the user (auto-generated)    |
| `user1`         | ForeignKey   | Name of the user1                                  |
| `user2`         | ForeignKey   | Name of the user2                                  |
| `match_score`   | Decimal      | Match score of users                               |
| `status`        | String       | Match status                                       |
| `created_on`    | DateTime     | Timestamp of record creation                       |
| `updated_on`    | DateTime     | Timestamp of last update                           |




# 5.Subscription APP
## Endpoints:
## 5.1 Create Subscription
* POST /subscriptions/
* Request Body:

```json
{
   
    "plan_type": "Premium"
}
```
* In Headers add key Authorization and value as token like this Token a542f2da1d0c79ed398e8862e582f17e3b744b9c
* Response:
    - Status 201: Created a new subscription.
    - Status 400: Validation error or missing required fields.

## 5.2 Retrive Subscription
* GET /subscription//
* Response:
    - Status 200: Returns a list of students, sorted by the specified subject marks.
    - Status 404: If no students are found or the subject parameter is incorrect.


### Models
#### Subscription
| Field           | Type         | Description                                           |
|-----------------|--------------|-------------------------------------------------------|
| `id`            | Integer      | Unique identifier for the user (auto-generated)    |
| `user    `      | ForeignKey   | ID of the user                                     |
| `plan_type`     | String       | plantype of user                                   |
| `status`        | String       | Current status of user                             |
| `start_date`    | DateTime     | Timestamp of record creation                       |
| `end_date`      | DateTime     | Timestamp of last update                           |


# 6.Message APP
## Endpoints:
## 6.1 Send Message
* POST /send-matching-message/
* Request Body:

```json
{
    "user1_id": 1,
    "user2_id": 2
}
```
* In Headers add key- Authorization and value- as  Token a542f2da1d0c79ed398e8862e582f17e3b744b9c  for admin authorization
* Response:
    - Status 404: If no User are found or the User parameter is incorrect.
    - Status 400: Validation error or missing required fields.
    - Status 201: Message send to both users.

## 6.2 Retrive Message
* GET /get-read-message/{message_id}/

* Response:
    - Status 200: Retrived message data.
    - Status 404: User not found.
    - Status 403: Only admins can send messages
    - Status 500: Internal server error


### Models
#### Message

| Field           | Type         | Description                                           |
|-----------------|--------------|-------------------------------------------------------|
| `id`            | Integer      | Unique identifier for the user (auto-generated)    |
| `sender`        | ForeignKey   | Name of the sender                                 |
| `receiver`      | ForeignKey   | Name of the  receiver                              |
| `message_text`  | Text         | Message details                                    |
| `status`        | String       | message read/unread status                         |
| `created_on`    | DateTime     | Timestamp of record creation                       |
| `updated_on`    | DateTime     | Timestamp of last update                           |


# 7. Notification APP
## Endpoints:
## 7.1 Send Notification for Incomplete Profile
* GET /notifications/incomplete-profile/{notification_id}/
* In Headers add key- Authorization and value- as  Token a542f2da1d0c79ed398e8862e582f17e3b744b9c  for admin authorization
* Response:
    - Status 200: Send messages for incomplete profile
  
## 7.2 Send Notification for Unread messages
* GET /notifications/unread-messages/{notification_id}/
* In Headers add key- Authorization and value- as  Token a542f2da1d0c79ed398e8862e582f17e3b744b9c  for admin authorization
* Response:
    - Status 200: Send messages for Unread messages
  
## 7.3 Bulk Notification
* POST /notifications/festival/
* Request Body:

```json
{
  "festival_name": "Diwali",
  "message": "Happy Diwali! May your life be filled with light and happiness.",
  "user_ids": [1, 2, 3, 4]
}
```
* In Headers add key- Authorization and value- as  Token a542f2da1d0c79ed398e8862e582f17e3b744b9c  for admin authorization
* Response:
    - Status 201: Created a new subscription.
    - Status 400: Validation error or missing required fields.

## 7.4 Send Notification for Unread notifications
* GET /notifications/unread/{notification_id}/
* In Headers add key- Authorization and value- as  Token a542f2da1d0c79ed398e8862e582f17e3b744b9c  for admin authorization
* Response:
    - Status 200: Send messages for Unread notification
  

### Models
#### Notification

| Field           | Type         | Description                                           |
|-----------------|--------------|-------------------------------------------------------|
| `id`            | Integer      | Unique identifier for the user (auto-generated)    |
| `user  `        | ForeignKey   | Name of the user                                   |
|`notification_type`| String     | Notification type                             |
| `message`       | Text         | Message details                                    |
| `status`        | String       | message read/unread status                         |
| `created_on`    | DateTime     | Timestamp of record creation                       |
| `updated_on`    | DateTime     | Timestamp of last update                           |




# 8.Master Code APP
## Endpoints:
## 8.1 Create Master Code
* POST /mastercodes/
* Request Body:

```json
{
  "type": "Religion",
  "code": "Hindu",
  "name": "Hindu",
  "display_text": "Hindu"
}
```
* Response:
    - Status 201: Created a new MasterCode.
    - Status 400: Validation error or missing required fields.


## 8.2 Update Master Code
* PUT /mastercodes/{master_code_id}/
* Request Body:

```json
 {
        "type": "caste",
        "code": "menon",
        "name": "Menon",
        "display_text": "Menon",
        "parent_code": 1
 }
 ```
* Response:
    - Status 404: If no details  found or the  details are incorrect.
    - Status 400: Validation error or missing required fields.
    - Status 200: Code successfully Updated.
```json
{
  "message": "Master code updated successfully."
}
```
## 8.3 Delete Master Code
* DELETE /mastercodes/{master_code_id}/
*  Response:
    - Status 204: No content, successful deletion.

```json
{
  "message": "Master code deleted successfully."
}
```

### Models
#### Master code
| Field           | Type         | Description                                           |
|-----------------|--------------|-------------------------------------------------------|
| `id`            | Integer      | Unique identifier for the user (auto-generated)    |
| `type   `       | String       | type of data                                       |
| `code`          |  String       | code of data                                      |
| `name`          | String       | name of data                                       |
| `display_text`  | String       | Display of code                                    |
| `created_on`    | DateTime     | Timestamp of record creation                       |
| `updated_on`    | DateTime     | Timestamp of last update                           |




Conclusion
This API documentation provides an overview of all
