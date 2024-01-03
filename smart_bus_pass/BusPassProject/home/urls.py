from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login_student',views.login_student, name="login"),
    path('register',views.register,name="register"),
    path('student_dashboard', views.student_dashboard, name='student_dashboad'),
    path('profile', views.profile, name='profile'),
    path('set_route', views.set_route, name='set_route'),
    path('view_route', views.view_route, name='view_route'),
    path('verification',views.verification, name='verification'),
    path('generate_pass',views.generate_pass, name='generate_pass'),
    path('college_dashboard',views.college_dashboard, name='college_dashboard'),
    path('student_verification',views.student_verification, name='student_verification'),
    path('verified_student',views.verified_student, name='verified_student'),
    path('manager_dashboard',views.manager_dashboard, name='manager_dashboard'),
    path('approval',views.approval, name='approval'),
    path('generate',views.generate, name='generate'),
    path('report',views.report, name='report')
]