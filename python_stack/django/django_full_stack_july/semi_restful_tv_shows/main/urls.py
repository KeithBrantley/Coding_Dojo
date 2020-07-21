from django.urls import path
from . import views

urlpatterns = [
    path('shows/new', views.index),
    path('add_a_show', views.add_a_show),
]
