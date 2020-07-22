from django.urls import path
from . import views

urlpatterns = [
    path('shows/new', views.add_a_show),
    path('shows/create', views.create_show),
    path('shows/<int:show_id>', views.show_info),
    path('shows/<int:show_id>/delete', views.delete),
    path('shows', views.all_shows),
    path('shows/<int:show_id>/edit', views.edit),
    path('shows/<int:show_id>/update', views.update),


]
