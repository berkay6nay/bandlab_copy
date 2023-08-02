from django.urls import path
from .views import ArtistSignUpView,RegularSignUpView

urlpatterns =  [
    
    path("signup_artist/" , ArtistSignUpView.as_view() , name="artist_signup"),
    path("signup_fan/" , RegularSignUpView.as_view() , name = "fan_signup"),
    
]