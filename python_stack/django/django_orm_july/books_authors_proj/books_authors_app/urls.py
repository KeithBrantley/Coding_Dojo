from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add_book', views.add_book),
]
