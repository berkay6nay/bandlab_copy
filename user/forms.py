from django import forms
from django.contrib.auth.forms import UserCreationForm 

from .models import User


class RegularSignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields

class ArtistSignupForm(UserCreationForm):
    ##artist_or_band_name = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields ##+ ("artist_or_band_name" , )
        



