from django.urls import path
from .views import (HomePageView , CreateArtistProfilePageView , ArtistProfilePageView , 
                    AlbumPageView , CreateAlbumView , EditArtistProfileView,DiscoDetailView,
                    EditAlbumView,DeleteAlbumView , CreateUserProfileView , UserProfilePageView,
                    EditUserProfileView , WishlistView)

urlpatterns = [
    path("" , HomePageView.as_view() , name = "home"),
    path("artist_profile_page/<int:pk>" , ArtistProfilePageView.as_view() , name = "artist_profile_page"),
    path("create_artist_profile_page" , CreateArtistProfilePageView.as_view() , name = "create_artist_profile_page"),
    path("album_page/<int:pk>" , AlbumPageView.as_view() , name="album_page"),
    path("create_album" ,CreateAlbumView.as_view() , name="create_album"),
    path("edit_artist_profile/<int:pk>" , EditArtistProfileView.as_view() , name = "edit_artist_profile"),
    path("disco_detail/<int:pk>" , DiscoDetailView.as_view() , name = "disco_detail"),
    path("album_edit/<int:pk>" , EditAlbumView.as_view() , name="edit_album"),
    path("album_delete/<int:pk>" , DeleteAlbumView.as_view() , name = "delete_album"),
    path("create_user_profile_page" ,CreateUserProfileView.as_view() , name = "create_user_profile_page"),
    path("user_profile_page/<int:pk>" , UserProfilePageView.as_view() , name = "user_profile_page"),
    path("edit_user_profile/<int:pk>" , EditUserProfileView.as_view() , name = "edit_user_profile"),
    path("add_to_wishlist/<int:pk>" , WishlistView , name = "add_to_wishlist")


]