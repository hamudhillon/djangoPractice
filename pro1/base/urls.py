from django.urls import path
from .views import *
# APP
urlpatterns = [
    path('home/',home),
    path('about/',about),
    path('aasdhgashd asjasdasd/<int:num1>/<int:num2>/<str:name>',add,name='add'),


    path('data/',data,name='data'),
    path('user/<str:name>',bio,name='bio'),

    path('createUsers/',createUsers,name='createUser')
]
