from django.urls import path
from .views import *

# APP
urlpatterns = [
    path('all/',blogAll,name='blogAll'),  
    path('<int:id>/<str:bname>',blogSingle,name='blogSingle'),  
    path('addPost/',addPost,name='addPost'),  
    path('signup/',signup,name='signup'),  
    path('logout/',userlogout,name='logout'),  
    path('profileUpdate/',profileUpdate,name='profileUpdate'),  

]
