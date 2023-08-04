from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView 
from django.views.generic import TemplateView
from .forms import RegularSignUpForm , ArtistSignupForm

class ArtistSignUpView(CreateView):
    form_class = ArtistSignupForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup_artist.html"
    

    def form_valid(self , form):
        form.instance.is_artist = True
        return super().form_valid(form)

class RegularSignUpView(CreateView):
    form_class = RegularSignUpForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup_fan.html"





# Create your views here.
