
from django.urls import path,include
from .views import *
# from rest_framework.routers import DefaultRouter

# router=DefaultRouter()
# router.register(r'students',StudentListCreate.as_view(),n=)

urlpatterns = [
    # path('',include(router.urls)),
    path('students/',StudentListCreate.as_view(),name="student-list-create"),
    path('students/<int:pk>',StudentDetail.as_view(),name="student-detail"),
    path('login/',LoginView.as_view(),name="login"),
]
