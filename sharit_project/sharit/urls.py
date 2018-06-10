
from django.urls import path
from . import views

urlpatterns = [
    # FOR testing Hello World success
    # path('', views.hello_world),
    # if we go to '/', go to the views, run the artist_list function.
    # third argument is naming this path.
    path('', views.post_list, name='post_list'),
    path('posts/<int:pk>', views.post_detail, name='post_detail'),
    path('posts/new', views.post_create, name='post_create'),
    path('posts/<int:pk>/edit', views.post_edit, name='post_edit'),
    path('posts/<int:pk>/delete', views.post_delete, name='post_delete'),    
]
