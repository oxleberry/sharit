
from django import forms
from django.forms import CharField, PasswordInput
from django.contrib.auth.models import User

from .models import Post, Comment


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'link', 'topic',)


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text', 'post',)

class LoginForm(forms.ModelForm):
    username = CharField(max_length=100)
    password = CharField(widget=PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password',)
