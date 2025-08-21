from django.urls import path
from .views import *
# APP
urlpatterns = [
    path('home/',home,name='home'),
    path('contact/',contact,name='contact'),
    path('student/',studentView,name='student'),
    path('about/',about,name='about'),
    path('aasdhgashd asjasdasd/<int:num1>/<int:num2>/<str:name>',add,name='add'),
    path('data/',data,name='data'),
    path('user/<str:name>',bio,name='bio'),
    path('createUsers/',createUsers,name='createUser'),
    path('empData',empViews,name='empData'),
    path('empCreate',empCreate,name='empCreate'),
    path('empDelete/<int:id>',empDelete,name='empDelete'),
    path('empUpdate/<int:id>',empUpdate,name='empUpdate'),
]
