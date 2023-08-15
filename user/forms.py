from django import forms
from django.contrib.auth.forms import UserCreationForm 

from .models import User


class RegularSignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields

class ArtistSignupForm(UserCreationForm):
    

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields 
        labels = {
            'username' : 'Artist or Band Name'
        }



