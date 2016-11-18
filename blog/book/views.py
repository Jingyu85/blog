from django.shortcuts import render

from article.models import Book

def book(request):
    '''
    Render the article page
    '''
    books = book.objects.all()
    context = {'books':books}
    return render(request, 'book/book.html', context)