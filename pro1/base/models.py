from django.db import models

# Create your models here.
class emp(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    address=models.TextField()
    department=models.CharField(max_length=50)