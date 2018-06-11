
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
# from django.contrib.auth import views as auth_views
# from django.conf.urls import include, url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sharit.urls')),
    # path('accounts/', include('django.contrib.auth.urls')),
    # path('login/', auth_views.login, name='login'),
    # path('logout/', auth_views.logout, name='logout'),
]
