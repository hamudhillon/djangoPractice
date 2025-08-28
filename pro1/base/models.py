from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta


class department(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
# Create your models here.
class emp(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    address=models.TextField()
    # department=models.CharField(max_length=50)
    department=models.ForeignKey(department,on_delete=models.CASCADE)


class student(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    age=models.CharField(max_length=10)
    


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    last_activity=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.user.username
    
    @property
    def is_online(self):
        return timezone.now() - self.last_activity < timedelta(minutes=5)
    
    @property
    def last_seen(self):
        diff=timezone.now() - self.last_activity
        minutes=int(diff.total_seconds() / 60)
        if minutes<1:
            return "just now"
        elif minutes < 60:
            return f"{minutes} min ago"
        elif minutes < 1440:
            hours=minutes // 60
            return f"{hours} hr ago" 
        else:
            days=minutes // 1440
            return f"{days} day(s) ago"