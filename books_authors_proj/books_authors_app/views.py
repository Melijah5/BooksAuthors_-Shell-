from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def index(request):
    context = {
        'all_books' : Book.objects.all(),
        'all_authors' : Author.objects.all(),
        
               }
    return render(request, 'index.html' , context)

def authors(request):
    context = {
        'authors': Author.objects.all(),
    }
    
    return render(request, 'authors.html', context)

def add_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST['desc']
        # book_id = request.POST['book_id']
        Book.objects.create(title=title, desc=desc)
    return redirect('/')

def edit_book(request, book_id):
    book_to_edit = Book.objects.get(id=book_id)
    authors = Author.objects.all()
    context = {
        'books' : book_to_edit,
        'authors' : authors
    }
    
    return render(request, 'books.html' , context)

def add_author(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        Author.objects.create(first_name=first_name, last_name=last_name)
    return redirect('/')

def edit_author(request, author_id):
    author_to_edit = Author.objects.get(id=author_id)
    books = Book.objects.all()
    context = {
        'author': author_to_edit,
        'books':books
    }
    return render(request, 'author_display.html', context)

def add_author_to_book(request, book_id):
    
    options = Author.objects.get(id=request.POST['select_author'])
    Book.objects.get(id=book_id).authors.add(options)
    return redirect(f'/books/{book_id}')
    
    
    # if request.method == 'POST':
    #     book_id = request.POST['book_id']
    #     author_id = request.POST['author_id']
    #     book = Book.objects.get(id=book_id)
    #     author = Author.objects.get(id=author_id)
    #     author.books.add(book)
    # return redirect(f"/authors/{author_id}")

def add_book_to_author(request, author_id):
    
    options = Book.objects.get(id=request.POST['select_book'])
    Author.objects.get(id=author_id).books.add(options)
    return redirect(f'/authors/{author_id}')
    
    
    # if request.method == 'POST':
    #     book_id = request.POST['book_id']
    #     author_id = request.POST['author_id']
    #     book = Book.objects.get(id=book_id)
    #     author = Author.objects.get(id=author_id)
    #     book.authors.add(author)
    # return redirect(f"/books/{book_id}")


