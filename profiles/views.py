from typing import Any, Dict
from django.shortcuts import render , get_object_or_404 
from django.views.generic import TemplateView , DetailView , CreateView , UpdateView , DeleteView , ListView
from django.urls import reverse_lazy , reverse
from .models import ArtistProfile , Album , UserProfile
from django.http import HttpResponseRedirect 

class HomePageView(TemplateView):
    template_name = "home.html"


class ArtistProfilePageView(DetailView):
    model = ArtistProfile
    template_name = "artist_profile_page.html"

    def get_context_data(self , *args , **kwargs):

        context = super(ArtistProfilePageView , self).get_context_data()
        page_user = get_object_or_404(ArtistProfile , id = self.kwargs["pk"])
        user = self.object.user
        logged_in_user = self.request.user
        albums = Album.objects.filter(artist = user)
        followed_artists = ArtistProfile.objects.filter(follower = logged_in_user)
        context["page_user"] = page_user
        context['albums'] = albums
        context["followed_artists"] = followed_artists
        
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

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:

        context = super(AlbumPageView , self).get_context_data()
        user = self.request.user
        album_artist = self.object.artist
        user_wishlist = Album.objects.filter(wishlists = user)
        context["user_wishlist"] = user_wishlist
        context["album_artist"] = album_artist


        return context


    template_name = "album_page.html"


class CreateAlbumView(CreateView):
    model = Album 
    template_name = "create_album.html"
    success_url = reverse_lazy("home")

    fields = ["album_pic" , "title" , "label" , "year" , "genre"]

    def form_valid(self , form):
        form.instance.artist = self.request.user
        return super().form_valid(form)
    

class EditArtistProfileView(UpdateView):
    model  = ArtistProfile
    template_name = "edit_artist_profile.html"
    fields = ["artist_bio" , "artist_pic"]
    success_url = reverse_lazy("home")


class DiscoDetailView(DetailView):
    
    model = ArtistProfile
    template_name = "edit_disco.html"

    def get_context_data(self , *args , **kwargs):

        context = super(DiscoDetailView , self).get_context_data()
        page_user = get_object_or_404(ArtistProfile , id = self.kwargs["pk"])
        user = self.object.user
        albums = Album.objects.filter(artist = user)
        context["page_user"] = page_user
        context['albums'] = albums
        
        return context
    
class EditAlbumView(UpdateView):
    model = Album
    template_name = "edit_album.html"
    fields = ["album_pic" , "title" , "label" , "year" , "genre"]
    success_url = reverse_lazy("home")

class DeleteAlbumView(DeleteView):
    model = Album
    template_name = "delete_album.html"
    success_url = reverse_lazy("home")

class CreateUserProfileView(CreateView):
    model = UserProfile

    fields = [
        
        "bio",
        "user_pic"
    ]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


    template_name = "create_user_profile.html"
    success_url = reverse_lazy("home")


class UserProfilePageView(DetailView):
    model = UserProfile
    template_name = "user_profile_page.html"
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super(UserProfilePageView , self).get_context_data()
        page_user = get_object_or_404(UserProfile , id = self.kwargs["pk"])
        wishlist_albums = Album.objects.filter(wishlists=page_user.user)
        followed_artists = ArtistProfile.objects.filter(follower = page_user.user)
        context["wishlist_albums"] = wishlist_albums
        context["followed_artists"] = followed_artists
        context["page_user"] = page_user
        return context
    
class EditUserProfileView(UpdateView):
    model = UserProfile

    fields = [
        "user_pic",
        "bio",
        "location",
    ]
    template_name = "edit_user_profile.html"
    success_url = reverse_lazy("home")

def WishlistView(request , pk):
    album = get_object_or_404(Album , id = pk)
    album.wishlists.add(request.user)
    return HttpResponseRedirect(reverse("album_page" , args=[str(pk)]))

class SearchResultsView(ListView):
    context_object_name = 'results'
    template_name = "search_results.html"
    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        album_list = Album.objects.filter(title__icontains = query)  if query else []
        artist_list = ArtistProfile.objects.filter(artist_name__icontains = query) if query else []
        return {
            "albums" : album_list,
            "artists" : artist_list,
        }
    
def FollowerView(request , pk):
    artist = get_object_or_404(ArtistProfile , id  = pk)
    artist.follower.add(request.user)
    return HttpResponseRedirect(reverse("artist_profile_page" , args=[str(pk)]))
# Create your views here.
