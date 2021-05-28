from django.db import models
from django.contrib.auth import get_user_model
from cloudinary.models import CloudinaryField

# Create your models here.
User = get_user_model()


class Profile(models.Model):
    """
    Profile class containing user model
    """
    user = models.ForeignKey(User, blank=False, on_delete=models.CASCADE)
    profile_picture = CloudinaryField()
    bio = models.CharField(max_length=300, blank=True, null=True)
    phone_number = models.CharField(max_length=10)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return f'{self.user.username}'


