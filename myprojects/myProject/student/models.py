from django.db import models
from django.utils import timezone

# Create your models here.

class Student(models.Model):
    id = models.AutoField(auto_created = True,primary_key = True)
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    age = models.IntegerField(default=-1)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    created_date = models.DateTimeField(default=timezone.now)
