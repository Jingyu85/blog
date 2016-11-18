from django.shortcuts import render, redirect
from django.contrib import messages

from article.models import Article, Comment
from article.forms import ArticleForm


def article(request):
    '''
    Render the article page
    '''
    articles = Article.objects.all()
    itemsList = []
    for article in articles:
        items = [article]
        items.extend(list(Comment.objects.filter(article=article)))
        itemsList.append(items)
    context = {'itemsList':itemsList}
    return render(request, 'article/article.html', context)

def articleCreate(request):
    '''
    Create a new article instance
    1. If method is GET, render an empty form
    2 . If method is POST, perform form validation. Display error messages if the form is invalid
    3. Save the form to the model and redirect to the article page
    '''
    template = 'article/articleCreate.html'
    if request.method == 'GET':
        return render(request, template, {'articleForm':ArticleForm()})
    # POST
    articleForm = ArticleForm(request.POST)
    if not articleForm.is_valid():
        return render(request, template, {'articleForm':articleForm})
    articleForm.save()
    messages.success(request, '文章已新增')
    return redirect('article:article')
    # Or try this at the last line: return article(request)