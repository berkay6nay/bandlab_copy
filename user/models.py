from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=False ,default="example@gmail.com" , null=True)
    is_artist = models.BooleanField(default=False)





# Create your models here.
