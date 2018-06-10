from django.http import HttpResponse
from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
from .forms import PostForm, CommentForm
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
    link = post.link
    small_link = link.split("=",1)[1]
    return render(request, 'sharit/post_detail.html', {'post': post, 'small_link': small_link})

# Post CREATE
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'sharit/post_form.html', {'form': form})

# Post EDIT/UPDATE
def post_edit(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'sharit/post_form.html', {'form': form})

# Post DELETE
def post_delete(request, pk):
    Post.objects.get(id=pk).delete()
    return redirect('post_list')

# Comment INDEX
def comment_list(request):
    comments = Comment.objects.all()
    return render(request, 'sharit/comment_list.html', {'comments': comments})

# Comment SHOW
def comment_detail(request, pk):
    comment = Comment.objects.get(id=pk)
    return render(request, 'sharit/comment_detail.html', {'comment': comment})

# Comment CREATE
def comment_create(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        print(form)
        if form.is_valid():
            comment = form.save()
            return redirect('comment_detail', pk=comment.pk)
    else:
        form = CommentForm()
        posts = Post.objects.all()
    return render(request, 'sharit/comment_form.html', {'form': form})

# Comment EDIT/UPDATE
def comment_edit(request, pk):
    comment = Comment.objects.get(pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save()
            return redirect('comment_detail', pk=comment.pk)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'sharit/comment_form.html', {'form': form})

# Comment DELETE
def comment_delete(request, pk):
    Comment.objects.get(id=pk).delete()
    return redirect('comment_list')
