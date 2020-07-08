from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('process_dojo', views.process_dojo),
    path('process_ninja', views.process_ninja),
    path('delete_dojo/<str:dojo_id>', views.delete_dojo),
]
