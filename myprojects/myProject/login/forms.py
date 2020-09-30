from django import forms
# import GeeksModel from models.py
from .models import Person

class UserForm(forms.Form):
    fname = forms.CharField(label='Your f name', max_length=10)
    lname = forms.CharField(label='Your l name', max_length=8)
    address = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()

# create a ModelForm
class PersonForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Person
        # fields = "__all__"
        fields = ["firstName", "lastName", "age","city", "address"]