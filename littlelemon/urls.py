"""
littlelemon URL Configuration

"""
from django.contrib import admin
from django.urls import path, include

from rest_framework.authtoken.views import obtain_auth_token #import obtain_auth_token view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurant/', include('restaurant.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('api-token-auth/', obtain_auth_token),
]
