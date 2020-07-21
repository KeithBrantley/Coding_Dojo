from django.urls import path
from . import views

urlpatterns = [
    path('shows/new', views.index),
]
