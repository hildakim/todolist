from django.contrib import admin
from django.urls import path
from .views import *

app_name = "user"

urlpatterns = [
    path('profile/', user_profile, name='profile'),
    path('profile/update/', user_profile_update, name='profile_update'),
    path('delete', user_profile_delete, name='profile_delete'),
]