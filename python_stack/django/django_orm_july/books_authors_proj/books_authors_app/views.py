from django.shortcuts import render, redirect
from .models import Book, Author

# Create your views here.

def index(request):
    context = {
        'all_books': Book.objects.all(),
        'all_authors': Author.objects.all(),
    }
    return render(request, 'add_book.html', context)

def add_book(request):
    Book.objects.create(
        title=request.POST['title'], 
        desc=request.POST['description']
        )
    return redirect('/')

def view_book(request, book_id):
    context = {
        'book_id': Book.objects.get(id=book_id),
    }
    return render(request, 'view_book.html', context)
