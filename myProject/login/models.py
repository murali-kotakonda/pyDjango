from django.db import models
from django.utils import timezone

CITIES = (
    ('hyd','HYDERABAD'),
    ('bang', 'BANGALORE'),
    ('mum','MUMBAI'),
    ('che','CHENNAI')
)



# Create your models here.
class Person(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    firstName = models.CharField(max_length=8)
    lastName = models.CharField(max_length=30)
    age = models.IntegerField(default=-1)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=6, choices=CITIES, default='hyd')
    created_date = models.DateTimeField(default=timezone.now)

#onetoone
class Addr(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    zip = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id)

class Emp(models.Model):
    id = models.AutoField(auto_created = True,primary_key = True)
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    currAddr = models.OneToOneField(Addr, on_delete=models.CASCADE)

#one to many
"""
one to many / many to one:
--------------------------------

one cust has multiple accounts


customer:
------
id   (PK)
name
age


account:
-------------
id   (PK)
name
custid  (FK) refers to id column for customer
created_date


one cust has many accounts----> one to many
multiple accounts belongsto onecustomer --> many to one


"""
class Customer(models.Model):
   id = models.AutoField(auto_created=True, primary_key=True)
   name = models.CharField(max_length=50)
   age = models.IntegerField()

   def __str__(self):
       return str(self.id)


class Account(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=50)
    custId = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)


#many to many

class Student(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=30)
    mobileNo = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Course(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    courseName = models.CharField(max_length=30)
    students = models.ManyToManyField(Student)

    def __str__(self):
        return self.courseName
