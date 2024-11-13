from django.urls import path
from .views import CreateUser, ListUser, UserDetail,LoginView

urlpatterns = [
    path('user/', ListUser.as_view(), name='list_users'),          # GET all users
    path('user/create/', CreateUser.as_view(), name='create_user'), # POST create user
    path('user/<int:pk>/', UserDetail.as_view(), name='user_detail'), # GET, PUT, DELETE user by ID
    path('login/', LoginView.as_view(), name='login_user'),          # GET all users

]
