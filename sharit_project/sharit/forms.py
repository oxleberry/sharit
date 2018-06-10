
from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'link', 'topic',)


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text', 'post')
