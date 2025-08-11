from django.db import models


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