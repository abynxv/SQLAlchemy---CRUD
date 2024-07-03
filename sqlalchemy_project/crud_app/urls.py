from django.urls import path
from . import views

urlpatterns = [
    path('colleges/', views.college_list),
    path('colleges/<int:pk>/', views.college_detail),
    path('students/', views.student_list),
    path('students/<int:pk>/', views.student_detail),
]
