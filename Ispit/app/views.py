from django.shortcuts import render, redirect
from .models import Book, Author
from .forms import BookForm


def index(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'index.html', context)


def add(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user
            book.save()
            authors_cleaned_data = form.cleaned_data['author_text']
            authors_data = authors_cleaned_data.split(',')
            for author in authors_data:
                author_name = author.strip()
                author = Author.objects.filter(name=author_name).first()
                if author:
                    author.save()
                    book.authors.add(author)

        return redirect('index')
    else:
        form = BookForm()
        context = {
            'form': form
        }
    return render(request, 'edit.html', context)


def edit(request, id):
    book_instance = Book.objects.filter(id=id).get()
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book_instance)
        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user
            book.save()
            authors_cleaned_data = form.cleaned_data['author_text']
            authors_data = authors_cleaned_data.split(',')
            book.authors.clear()
            for author in authors_data:
                author_name = author.strip()
                author = Author.objects.filter(name=author_name).first()
                if author:
                    author.save()
                    book.authors.add(author)

        return redirect('index')
    else:
        form = BookForm(instance=book_instance)
    return render(request, 'edit.html', {'form': form})

def delete(request, id):
    book_instance = Book.objects.filter(id=id).get()
    if request.method == 'POST':
        book_instance.delete()
        return redirect('index')
    return render(request, 'delete.html')