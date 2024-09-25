from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    linkedin_email = models.EmailField()
    linkedin_password = models.CharField(max_length=255)
    job_titles = models.TextField()
    locations = models.TextField()
    experience_level = models.CharField(max_length=50)
    job_types = models.TextField()
    remote = models.BooleanField(default=False)
    easy_apply = models.BooleanField(default=True)
    keywords = models.TextField(blank=True)

    def __str__(self):
        return self.user.username
