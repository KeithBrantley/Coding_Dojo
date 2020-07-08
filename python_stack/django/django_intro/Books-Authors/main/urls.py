from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('process_book', views.process_book),
    path('book/<int:book_id>', views.book_info),
    path('author', views.author),
    path('process_author', views.process_author),
    path('author/<int:author_id>', views.author_info),
]
