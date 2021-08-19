from django.contrib import admin
from django.urls import path
from .views import *

app_name = "todo"

urlpatterns = [
    path('', todo, name="home"),
    path('new/', new, name="new"),
    path('edit/<int:id>', edit, name="edit"),
    path('delete/<int:id>', delete, name="delete"),
    path('mail/', mail, name="mail"),
    path('completed/<int:id>', completed, name="complete"),
    path('search/', search, name="search"),
]