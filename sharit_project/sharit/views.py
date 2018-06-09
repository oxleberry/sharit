
from django.shortcuts import render
# from django.contrib.auth.models import User
# from .forms import Post, Comment, Profile
# from .models import Post, Comment, Profile

# FOR testing: HELLO WORLD SUCCESS
from django.http import HttpResponse
def hello_world(request):
    return HttpResponse('Hello Sharon')
