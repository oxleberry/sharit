
from django.contrib.auth import get_user_model
from django.db import models
# from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     bio = models.TextField(max_length=500, blank=True)
#     location = models.CharField(max_length=30, blank=True)
#
#     def __str__(self):
#         return self.user

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()

class Post(models.Model):
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    # photo = models.FileField(null=True, blank=True)
    topic = models.CharField(max_length=100)
    created_post = models.DateTimeField(auto_now_add=True)
    # comment_count = models.IntegerField()
    # vote_score = models.IntegerField()
    # profile = models.ForeignKey(get_user_model(),on_delete=models.CASCADE, related_name='post_profile')

    def __str__(self):
        return self.title

class Comment(models.Model):
    text = models.TextField()
    created_comment = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    # profile = models.ForeignKey(get_user_model(),on_delete=models.CASCADE, related_name='comment_profile')

    def __str__(self):
        return self.text
