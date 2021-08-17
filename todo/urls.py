from django.contrib import admin
from django.urls import path
from .views import *

app_name = "todo"

urlpatterns = [
    path('', todo, name="home"),
    path('<int:id>', detail, name="detail"),
    path('new/', new, name="new"),
    path('edit/<int:id>', edit, name="edit"),
    path('delete/<int:id>', delete, name="delete"),
]