from django.urls import path
from .views import *
# APP
urlpatterns = [
    path('all/',blogAll,name='blogAll'),  
    path('single/',blogSingle,name='blogSingle'),  
    path('addPost/',addPost,name='addPost'),  
]
