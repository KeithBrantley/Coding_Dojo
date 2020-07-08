from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('process_chef', views.process_chef),
    path('process_dish', views.process_dish),
    path('process_utensil', views.process_utensil),
    path('utensil/<int:utensil_id>', views.one_utensil),
    path('utensil/user/add', views.add_user_utensil),
]
