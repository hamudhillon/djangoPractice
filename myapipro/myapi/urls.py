
from django.urls import path
from .views import *
urlpatterns = [
    path('',home,name='home'),
    path('student_list',student_list,name='student_list'),
    path('student_details/<int:id>',student_details,name='student_details'),
]
