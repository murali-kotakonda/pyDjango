
from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.sessions.models import Session

from .models import Person
from .models import Addr
from .models import Emp
from .models import Customer
from .models import Account
from .models import Student
from .models import Course

# Register your models here.

class MyPersondmin(admin.ModelAdmin):
   		list_display = ('id','firstName', 'lastName', 'age', 'address','city','created_date')

class MyAddradmin(admin.ModelAdmin):
   		list_display = ('id','street','city','country','zip')

class MyEmpadmin(admin.ModelAdmin):
   		list_display = ('id','firstName', 'lastName','currAddr')


class MyCustomeradmin(admin.ModelAdmin):
   		list_display = ('id','name','age')
class MyAccountadmin(admin.ModelAdmin):
   		list_display = ('id','name','custId','created_date')


class MyStudentadmin(admin.ModelAdmin):
   		list_display = ('id','name','mobileNo')
class MyCourseadmin(admin.ModelAdmin):
   		list_display = ('id','courseName')




admin.site.register(Person, MyPersondmin)
admin.site.register(Addr, MyAddradmin)
admin.site.register(Emp, MyEmpadmin)
#admin.site.register(Customer, MyCustomeradmin)
#admin.site.register(Account, MyAccountadmin)
admin.site.register(Student, MyStudentadmin)
admin.site.register(Course, MyCourseadmin)



class SessionAdmin(ModelAdmin):
    def _session_data(self, obj):
        return obj.get_decoded()
    list_display = ['session_key', '_session_data', 'expire_date']
#admin.site.register(Session, SessionAdmin)
