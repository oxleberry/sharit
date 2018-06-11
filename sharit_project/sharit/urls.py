

# from django.conf.urls import url

from django.urls import path
from . import views

urlpatterns = [
    # FOR testing Hello World success
    # path('', views.hello_world),
    # if we go to '/', go to the views, run the artist_list function.
    # third argument is naming this path.
    path('signup', views.signup, name='signup'),
    path('login', views.login_user, name='login'),
    path('logout_user', views.logout_user, name='logout_user'),    
    path('', views.post_list, name='post_list'),
    path('posts/<int:pk>', views.post_detail, name='post_detail'),
    path('posts/new', views.post_create, name='post_create'),
    path('posts/<int:pk>/edit', views.post_edit, name='post_edit'),
    path('posts/<int:pk>/delete', views.post_delete, name='post_delete'),
    path('comments/', views.comment_list, name='comment_list'),
    path('comments/<int:pk>', views.comment_detail, name='comment_detail'),
    path('comments/new', views.comment_create, name='comment_create'),
    path('comments/<int:pk>/edit', views.comment_edit, name='comment_edit'),
    path('comments/<int:pk>/delete', views.comment_delete, name='comment_delete'),
]
