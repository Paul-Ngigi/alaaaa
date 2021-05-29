from django.db import models
from django.contrib.auth import get_user_model
from cloudinary.models import CloudinaryField
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
User = get_user_model()


class Profile(models.Model):
    """
    Profile class containing user model
    """
    user = models.ForeignKey(User, blank=False, on_delete=models.CASCADE, related_name="profile_user")
    profile_picture = CloudinaryField()
    bio = models.CharField(max_length=300, blank=True, null=True)
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return f'{self.user.username}'

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def find_by_username(cls, search_term):
        user = cls.objects.filter(user__username__icontains=search_term)
        return user


class Project(models.Model):
    title = models.CharField(max_length=30)
    project_screenshot = CloudinaryField()
    website_url = models.URLField()
    project_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Vote(models.Model):
    design = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    usability = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    creativity = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    content = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.project.title
