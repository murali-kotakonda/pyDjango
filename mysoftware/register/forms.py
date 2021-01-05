from django import forms
from .models import Person

# import GeeksModel from models.py


class PersonForm(forms.):
    # specify the name of model to use
    class Meta:
        model = Person
        # fields = "__all__"
        fields = ['id',"firstName", "lastName", "age",'email','userName','password' ,'userType','created_date']