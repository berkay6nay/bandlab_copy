from django.db import models
from user.models import User

class Album(models.Model):
    title = models.TextField(max_length=50 , editable=True)
    artist = models.ForeignKey(User , on_delete=models.CASCADE)
    album_pic = models.ImageField(null=True , blank=True , upload_to="images/" , editable=True)
    label = models.TextField(max_length= 30 , null=True , blank=True , editable=True)
    year = models.IntegerField(null=True , blank=True , editable=True)
    genre = models.CharField(max_length=30 , null=True , blank=True , editable=True)
    preview_song = models.FileField(blank=True , null= True , upload_to="audio/" , editable=True)
    wishlists = models.ManyToManyField(User , related_name="albums")
    buyed = models.ManyToManyField(User , related_name="album_buy")


class ArtistProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    artist_bio = models.TextField(max_length=100 , editable=True)
    artist_name = models.TextField(max_length=50)
    artist_pic = models.ImageField(null=True , blank=True ,upload_to="images/" , editable=True)
    follower = models.ManyToManyField(User , related_name="artists_follower")

    def __str__(self):
        return str(self.user)

class UserProfile(models.Model):
    name = models.TextField(max_length=50)
    user = models.OneToOneField(User , on_delete=models.CASCADE , null=True)
    user_pic = models.ImageField(blank=True , null=True , upload_to="images/" , editable=True)
    bio = models.TextField(blank=True , null=True  , max_length=1000 , editable=True)
    location = models.TextField(blank=True , null= True , max_length=50 , editable=True)


class Comment(models.Model):
    album = models.ForeignKey(Album,related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    body = models.TextField()





    


# Create your models here.
