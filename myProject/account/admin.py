from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Profile
from django.contrib.auth.models import User
from django.contrib import admin



class ProfileAdmin(admin.ModelAdmin):
    list_display = ( 'middle_name', 'dob', 'active', 'pub_date')

class UserAdmin(admin.ModelAdmin):
    list_display = ('middle_name', 'password', 'email', 'first_name','last_name')

#admin.site.register(Profile, ProfileAdmin)
#admin.site.register(User, UserAdmin)


