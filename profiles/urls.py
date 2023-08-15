from django.urls import path
from .views import HomePageView , CreateArtistProfilePageView , ArtistProfilePageView , AlbumPageView , CreateAlbumView

urlpatterns = [
    path("" , HomePageView.as_view() , name = "home"),
    path("artist_profile_page/<int:pk>" , ArtistProfilePageView.as_view() , name = "artist_profile_page"),
    path("create_artist_profile_page" , CreateArtistProfilePageView.as_view() , name = "create_artist_profile_page"),
    path("album_page/<int:pk>" , AlbumPageView.as_view() , name="album_page"),
    path("create_album" ,CreateAlbumView.as_view() , name="create_album"),
    

]