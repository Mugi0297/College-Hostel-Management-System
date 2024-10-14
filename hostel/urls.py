"""
URL configuration for hostel_management project.

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
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home1, name='home1'),
    path('students/', views.student_list, name='student_list'),
    path('add_student/', views.add_student, name='add_student'),
    path('submit_grievance/', views.submit_grievance, name='submit_grievance'),
    path('meal_count/', views.meal_count, name='meal_count'),
    path('view_meal_counts/', views.view_meal_counts, name='view_meal_counts'),
    path('mark_attendance/', views.mark_attendance, name='mark_attendance'),
    path('view_attendance/', views.view_attendance, name='view_attendance'),
    path('request_permission/', views.request_permission, name='request_permission'),
    path('grievance_report/', views.grievance_report, name='grievance_report'),
    path('view_permission_requests/', views.view_permission_requests, name='view_permission_requests'),  # New URL
    path('update_permission_request/<int:request_id>/', views.update_permission_request,
         name='update_permission_request'),  # Update URL
    path('report_grievance/', views.report_grievance, name='report_grievance'),
    path('view_grievances/', views.view_grievances, name='view_grievances'),
    path('update_grievance/<int:grievance_id>/', views.update_grievance_status, name='update_grievance_status'),

]
