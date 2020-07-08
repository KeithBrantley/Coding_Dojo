from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('new', views.new),
    path('create', views.create),
    path("<int:num>", views.show),
    path("<int:num>/edit", views.edit),
    path("<int:num>/delete", views.destroy),
]
