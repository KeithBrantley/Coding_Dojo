from django.shortcuts import render, redirect
from .models import Book, Author

# Create your views here.

def index(request):
    context={
        'all_books': Book.objects.all(),
    }
    return render(request, 'index.html',context)

def process_book(request):
    Book.objects.create(
        title=request.POST['title'],
        description=request.POST['description'],
    )
    return redirect('/')

def book_info(request, book_id):
    book = Book.objects.get(id=book_id)
    context={
        'this_book': book,
    }

    return render(request, 'book_info.html', context)

def author(request):
    context={
        'all_authors': Author.objects.all(),
    }
    return render(request, 'author.html', context)

def process_author(request):
    Author.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        notes=request.POST['notes']
    )
    return redirect('/author')

def author_info(request, author_id):
    author = Author.objects.get(id=author_id)
    context={
        'this_author': author,
    }

    return render(request, 'author_info.html', context)
