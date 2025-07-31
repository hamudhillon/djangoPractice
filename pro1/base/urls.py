from django.urls import path
from .views import *
# APP
urlpatterns = [
    path('home/',home),
    path('about/',about),
    path('aasdhgashd asjasdasd/<int:num1>/<int:num2>/<str:name>',add,name='add')
]
