from django.shortcuts import render, redirect
from .models import Book, Author

# Create your views here.

def index(request):
    context = {
        'all_books': Book.objects.all(),
    }
    return render(request, 'index.html', context)

def add_book(request):
    Book.objects.create(
        title=request.POST['title'], 
        desc=request.POST['description']
        )
    return redirect('/')

def view_book(request, book_id):
    context = {
        'book_id': Book.objects.get(id=book_id),
        'auth_id': Author.objects.all()
    }
    return render(request, 'view_book.html', context)

def author(request):
    context = {
        'all_authors': Author.objects.all(),
    }
    return render(request, 'author.html', context)

def add_author(request):
    Author.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        notes=request.POST['notes']
        )
    return redirect('/author.html')

def view_author(request, auth_id):
    context = {
        'auth_id': Author.objects.get(id=auth_id)
    }
    return render(request, 'view_author.html', context)