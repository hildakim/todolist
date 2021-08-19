from django.contrib import admin
from django.urls import path
from .views import *

app_name = "messenger"

urlpatterns = [
    path('detail_m/<str:id>', detail_m, name = "detail_m"),
    path('new_m/', new_m, name = "new_m"),
    path('send_m/', send_m, name = "send_m"),
    path('received_m/', receive_m, name = "received_m"),
    path('delete_m/<str:id>', delete_m, name = "delete_m"),
]