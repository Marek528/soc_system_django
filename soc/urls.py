from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('temy/', views.vypis_tem, name='vypis-tem'),
    path('ucitel/<id>/', views.vypis_ucitela, name='vypis-ucitela'),
    path('student/<id>/', views.vypis_studenta, name='vypis-studenta'),
    path('tema/<id>/', views.vypis_temy, name='vypis-temy'),
]