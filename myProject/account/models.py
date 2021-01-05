
from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    middle_name = models.CharField(max_length=30, blank=True)
    dob = models.DateField(null=True, blank=True)
    active = models.BooleanField(default=True)
    pub_date = models.DateTimeField(default=timezone.now)