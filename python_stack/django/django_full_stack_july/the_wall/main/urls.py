from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('wall', views.wall),
    path('login', views.login),
    path('post_message', views.message),
    # path('post_comment', views.comment),
    path('logoff', views.logoff),
]
