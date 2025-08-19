from venv import create
from django.db import models
from django.contrib.auth.models import User

class tag(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
class category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
# Create your models here.




class author(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    phone=models.CharField(max_length=100,blank=True)
    profilePic=models.ImageField(upload_to='users',blank=True)
    bio=models.TextField(blank=True)
    Fb_link=models.CharField(max_length=500,blank=True)
    ig_link=models.CharField(max_length=500,blank=True)
    X_link=models.CharField(max_length=500,blank=True)
    yt_link=models.CharField(max_length=500,blank=True)
class blog(models.Model):
    title=models.CharField(max_length=200)
    desc=models.TextField()
    tags=models.ManyToManyField(tag)
    category=models.ForeignKey(category,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='blog',blank=True)
    author=models.ForeignKey(author,on_delete=models.CASCADE,null=True,blank=True)
    created_at=models.DateTimeField()
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    
