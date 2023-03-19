from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    address = models.CharField(max_length=255, blank=True, null=True)
    contact = models.CharField(max_length=255, blank=True, null=True)


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
    profile_picture = models.ImageField(
        upload_to="profile_images", blank=True, null=True
    )
    about = models.CharField(max_length=1000, blank=True)
    location = models.CharField(max_length=100, blank=True)
