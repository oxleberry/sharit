
from django.urls import path
from . import views

urlpatterns = [
    # FOR testing Hello World success
    path('', views.hello_world),

    # if we go to '/', go to the views, run the artist_list function.
    # third argument is naming this path.
    # path('', views.post_list, name='post_list'),
]
