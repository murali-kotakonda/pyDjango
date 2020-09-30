from django.contrib import admin
from .models import Person


# Register your models here.
class MyPersondmin(admin.ModelAdmin):
   		list_display = ('id','firstName', 'lastName','age','email','userName','password' ,'userType','created_date')




admin.site.register(Person, MyPersondmin)
