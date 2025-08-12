from venv import create
from django.db import models


class tag(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
class category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
# Create your models here.
class blog(models.Model):
    title=models.CharField(max_length=200)
    desc=models.TextField()
    tags=models.ManyToManyField(tag)
    category=models.ForeignKey(category,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='blog',blank=True)
    author=models.CharField(max_length=100,blank=True)
    created_at=models.DateTimeField()
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title