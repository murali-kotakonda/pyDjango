from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id','firstName', 'lastName', 'age', 'username', 'password','created_date')

admin.site.register(Employee, EmployeeAdmin)

