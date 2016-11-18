from django.shortcuts import render

from article.models import Book


def book(request):
    '''
    Render the book page
    '''
    books = Book.objects.all()
    context = {'books':books}
    return render(request, 'book/book.html', context)