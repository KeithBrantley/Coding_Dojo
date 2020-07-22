from django.shortcuts import render, redirect
from .models import Book, Author

# Create your views here.

def index(request):
    context = {
        'all_books': Book.objects.all()
    }
    return render(request, 'index.html', context)

def create_book(request):
    Book.objects.create(
        title=request.POST['title'],
        description=request.POST['description']
    )
    return redirect('/')

def one_book(request, book_id):
    one_book = Book.objects.get(id=book_id)
    context = {
        "one_book": one_book
    }
    return render(request, 'one_book.html', context)

    # Author

def authors(request):
    context = {
        'all_authors': Author.objects.all()
    }
    return render(request, 'authors.html', context)

def create_author(request):
    Author.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        notes=request.POST['notes']
    )
    return redirect('/authors')

def one_author(request, author_id):
    one_author = Author.objects.get(id=author_id)
    context = {
        "one_author": one_author
    }
    return render(request, 'one_author.html', context)