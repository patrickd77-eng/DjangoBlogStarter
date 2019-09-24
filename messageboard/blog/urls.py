from django.contrib import admin
from django.urls import path
from . import views
from .views import PostListView

urlpatterns = [
    path('', PostListView.as_view(), name='board-home'),
    path('about/', views.about, name='board-about'),
    path('admin/', views.home, name='board-admin'),
]
