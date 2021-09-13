from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('snap/', views.resticsnapfile, name='resticsnapfile'),
    path('stats/', views.resticstats, name='resticstats'),
    path('restore/', views.resticrestore, name='resticrestore'),
    path('find/', views.resticfind, name='resticfind'),
]