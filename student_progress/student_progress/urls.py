"""
URL configuration for student_progress project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
#from app_student_progress.views import home  # Import the home view

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', home, name='home'),
    path('',include('app_student_progress.urls')),
    path('api/', include('app_student_progress.urls')),
    path('', include('app_teacher.urls')),
    path('', include('school.urls')),        # Routes /api/schools/ to school URLs
    path('', include('department.urls')), # Routes /api/departments/ to department URLs
    #path('users/',include('app_User.urls')),
    path('userapp/',include('userapp_new.urls')),
                ]       