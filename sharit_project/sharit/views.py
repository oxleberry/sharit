from django.http import HttpResponse
from django.shortcuts import render
# from django.contrib.auth.models import User
# from .forms import Post, Comment, Profile
from .models import Post, Comment

# FOR testing: HELLO WORLD SUCCESS
# from django.http import HttpResponse
# def hello_world(request):
#     return HttpResponse('Hello World')

# Post INDEX
def post_list(request):
    posts = Post.objects.all().order_by('title')
    return render(request, 'sharit/post_list.html', {'posts': posts})

# Post SHOW
def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'sharit/post_detail.html', {'post': post})
