from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('shows', views.all_shows),
    path('login', views.login),
    path('logout', views.logout),
    path('add_show', views.add_show),
    path('process_show', views.process_show),
]