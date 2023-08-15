from django.shortcuts import render , get_object_or_404
from django.views.generic import TemplateView , DetailView , CreateView
from django.urls import reverse_lazy
from .models import ArtistProfile , Album

class HomePageView(TemplateView):
    template_name = "home.html"


class ArtistProfilePageView(DetailView):
    model = ArtistProfile
    template_name = "artist_profile_page.html"

    def get_context_data(self , *args , **kwargs):

        context = super(ArtistProfilePageView , self).get_context_data()
        page_user = get_object_or_404(ArtistProfile , id = self.kwargs["pk"])
        user = self.object.user
        albums = Album.objects.filter(artist = user)
        context["page_user"] = page_user
        context['albums'] = albums
        
        return context


    


class CreateArtistProfilePageView(CreateView):
    model = ArtistProfile
    template_name = "create_artist_profile_page.html"

    fields = [
        "artist_name",
        "artist_pic",
        "artist_bio",
        ]
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy("home")


class AlbumPageView(DetailView):
    model = Album
    template_name = "album_page.html"


class CreateAlbumView(CreateView):
    model = Album 
    template_name = "create_album.html"

    fields = ["album_pic" , "title" , "label" , "year" , "genre"]

    def form_valid(self , form):
        form.instance.artist = self.request.user
        return super().form_valid(form)
    

    
       



    




# Create your views here.
