from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('temy/', views.vypis_tem, name='vypis-tem'),
]