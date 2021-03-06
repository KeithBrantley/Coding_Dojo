from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('process_book', views.create_book),
    path('book/<int:book_id>',views.one_book),
    path('author/<int:author_id>',views.one_author),
    path('authors', views.authors),
    path('process_author', views.create_author),
    path('add_auth_to_book', views.add_auth_to_book),
    path('add_book_to_auth', views.add_book_to_auth),
]
