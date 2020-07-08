from django.urls import path
from . import views

urlpatterns = [
    path('shows/new', views.add_new_show),
    path('shows/create', views.create_show),
    path('shows/<int:show_id>', views.show_details),
    path('shows/<int:show_id>/destroy', views.delete_show),
    path('shows', views.all_shows),
    path('shows/<int:show_id>/edit', views.edit),
    path('shows/<int:show_id>/update', views.update),
]