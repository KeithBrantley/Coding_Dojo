from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add_book', views.add_book),
    path('view_book/<int:book_id>', views.view_book),
    path('add_auth_to_book', views.add_auth_to_book),
    path('authors', views.author),
    path('add_author', views.add_author),
    path('view_author/<int:auth_id>', views.view_author),
]
