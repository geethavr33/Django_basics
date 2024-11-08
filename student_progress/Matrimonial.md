# MATRIMONIAL SITE
### 1. User Profile Module
  Purpose: Manage user details like name, age, gender, and contact information.
## 	Key Fields:
* 	user_id (Primary Key)
*	username, password (for authentication)
*	first_name, last_name, age, gender
* Religion
* Caste
* Height
* Gender
*	contact_details (One-to-One relationship for phone, email)
*	created_on, updated_on
##	APIs:
*	Register User (POST)
*	Login (POST)
*	Get User Profile (GET)
*	Update User Profile (PUT)
*	Delete User Profile (DELETE)
### 2. Partner Preferences Module
*	Purpose: Store the preferred partner attributes for matching.
*	Key Fields:
*	preference_id (Primary Key)
*	user_id (ForeignKey to User Profile)
*	preferred_age_range, preferred_location, preferred_occupation
*	marital_status, minimum_education, religion, caste
###	APIs:
*	Create Preferences (POST)
*	Get Preferences (GET)
*	Update Preferences (PUT)
*	Delete Preferences (DELETE)
## 3. Search & Match Module
*	Purpose: Allow users to search and view matched profiles.
*	Key Fields:
*	Uses User Profile and Partner Preferences details
###	APIs:
*	Search Profiles (GET, with filters for age, location, etc.)
*	Get Match Suggestions (GET, based on preferences)
*	Save to Favorites (POST, adds to the Favorites module)
## 4. Favorites Module
*	Purpose: Manage profiles that users have marked as favorites.
###	Key Fields:
*	favorite_id (Primary Key)
*	user_id (ForeignKey to User Profile)
*	favorited_user_id (ForeignKey to another User Profile)
*	created_on
###	APIs:
*	Add Favorite (POST)
*	Get Favorites List (GET)
*	Remove from Favorites (DELETE)
## 5. Communication Module
###	Purpose: Allow users to communicate via chat or messaging.
•	Key Fields:
*	message_id (Primary Key)
*	sender_id (ForeignKey to User Profile)
*	receiver_id (ForeignKey to User Profile)
*	message_content, timestamp
###	APIs:
*	Send Message (POST)
*	Get Chat History (GET)
*	Delete Message (DELETE)
## 6. Subscription Module
*	Purpose: Manage subscription plans for premium features.
###	Key Fields:
*	subscription_id (Primary Key)
*	user_id (ForeignKey to User Profile)
*	plan_name, price, start_date, end_date
*	is_active
### 	APIs:
*	Subscribe to Plan (POST)
*	Get Current Subscription (GET)
*	Cancel Subscription (DELETE)
## 7. Profile Verification Module
*	Purpose: Verify profiles through document uploads or moderator review.
*	Key Fields:
*	verification_id (Primary Key)
*	user_id (ForeignKey to User Profile)
*	status (e.g., Pending, Verified, Rejected)
*	uploaded_documents (file field for ID, photos)
###	APIs:
*	Submit Verification (POST)
*	Get Verification Status (GET)
*	Admin Review Verification (PUT for status update)
### 8. Admin Management Module
*	Purpose: For site administrators to manage users, content, and settings.
*	Key Fields:
*	admin_id (Primary Key)
*	role (e.g., Moderator, Super Admin)
*	permissions
###	APIs:
*	Get All Users (GET for admin use)
*	Ban User (PUT to disable a user profile)
*	Approve Verification (PUT in Verification module)
Postman API Testing
1.	Use Postman to test each API endpoint by setting up appropriate requests (e.g., authorization headers for protected routes).
2.	Use collections in Postman to group APIs by module for better organization.

