from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('dashboard', views.dashboard),
    path('create_new_trip_page', views.create_new_trip_page),
    path('create_trip', views.create_trip),
    path('edit_trip/<int:trip_id>', views.edit_trip),
    path('dashboard/update/<int:trip_id>', views.update),
    path('dashboard/view_trip/<int:trip_id>',views.view_trip),
    path('dashboard/delete/<int:trip_id>', views.delete),
    path('login', views.login),
    path('logout', views.logout),
]
