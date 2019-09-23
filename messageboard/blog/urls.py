from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='board-home'),
    path('about/', views.about, name='board-about'),
    path('admin/', views.about, name='board-admin'),
]
