from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('temy/', views.vypis_tem, name='vypis-tem'),
    path('ucitel/<id>/', views.vypis_ucitela, name='vypis-ucitela'),
    path('student/<id>/', views.vypis_studenta, name='vypis-studenta'),
    path('temy_samostatne/', views.vypis_tem_samostatne, name='vypis-tem-samostatne'),
    path('tema/<id>/', views.vypis_temy, name='vypis-temy'),
    path('statistiky/', views.statistiky, name='statistiky'),
    path('pridanie_temy/', views.pridat_temu, name='pridanie-temy'),
]