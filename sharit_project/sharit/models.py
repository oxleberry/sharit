from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    photo = models.FileField(null=True, blank=True)
    subreddit = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Comment(models.Model):
    com_text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.com_text

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    # post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    # comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.user

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
