from django.shortcuts import render
from .models import *


# Create your views here.
def blogAll(request):
    allBlogs=blog.objects.all()
    return render(request,'blogAll.html',context={'blogs':allBlogs})

def blogSingle(request):

    return render(request,'singleBlog.html')

def addPost(request):

    return render(request,'addBlog.html')