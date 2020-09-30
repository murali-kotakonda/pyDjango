from django.db import models
from django.utils import timezone

TYPES =(
    ('admin','ADMIN'),
    ('user','USER'),
)

# Create your models here.
class Person(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    firstName = models.CharField(max_length=8)
    lastName = models.CharField(max_length=6)
    age = models.IntegerField(default=-1)
    email=models.EmailField(max_length=10)
    userName = models.CharField(max_length=5)
    password= models.CharField(max_length=9)
    userType = models.CharField(max_length=6, choices=TYPES, default='admin')
    created_date = models.DateTimeField(default=timezone.now)
