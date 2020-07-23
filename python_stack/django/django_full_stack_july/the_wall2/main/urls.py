from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('wall', views.wall),
    path('login', views.login),
    path('logoff', views.logoff),

]
