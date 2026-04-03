from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=200, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    followers = models.ManyToManyField(User, related_name='following', blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

    def total_followers(self):
        return self.followers.count()

    def total_following(self):
        return Profile.objects.filter(followers=self.user).count()