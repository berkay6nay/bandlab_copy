from django.shortcuts import render 
from django.views.generic import TemplateView , DetailView , CreateView
from django.urls import reverse_lazy
from .models import ArtistProfile

class HomePageView(TemplateView):
    template_name = "home.html"


class ArtistProfilePageView(DetailView):
    model = ArtistProfile
    template_name = "artist_profile_page.html"

    


class CreateArtistProfilePageView(CreateView):
    model = ArtistProfile
    template_name = "create_artist_profile_page.html"

    fields = [
        "artist_name",
        "artist_pic",
        "artist_bio",
        ]
    def form_valid(self, form):
        form.instance.user_artist = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy("home")

    


    




# Create your views here.
