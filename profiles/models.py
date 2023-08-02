from django.db import models
from user.models import User

class Album(models.Model):
    title = models.TextField(max_length=50)
    artist = models.ForeignKey(User , on_delete=models.CASCADE)


class ArtistProfile(models.Model):
    artist = models.ForeignKey(User, on_delete=models.CASCADE)
    artist_bio = models.TextField(max_length=100)
    name = models.TextField(max_length=50)


class UserProfile(models.Model):
    name = models.TextField(max_length=50)


# Create your models here.
