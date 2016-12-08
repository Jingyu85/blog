from django.contrib import messages
from django.db.models.query_utils import Q
from django.shortcuts import render, redirect, get_object_or_404

from article.forms import ArticleForm
from article.models import Article, Comment


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
    template = 'article/articleCreateUpdate.html'
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
    
def articleRead(request, articleId):
    '''
    Read an article
        1. Get the "article" instance; redirect to the 404 page if not found
        2. Render the articleRead template with article instance and its
           associated comments
    '''
    articleToRead = get_object_or_404(Article, id=articleId)
    context = {
        'article': articleToRead,
        'comments': Comment.objects.filter(article=articleToRead)
    }
    return render(request, 'article/articleRead.html', context)

def articleUpdate(request, articleId):
    '''
    Update the article instance:
        1. Get the article to update; redirect to 404 if not found
        2. Render a bound form if the method is GET
        3. If the form is valid, save it to the model, otherwise render a
           bound form with error messages
    '''
    articleToUpdate = get_object_or_404(Article, id=articleId)
    template = 'article/articleCreateUpdate.html'
    if request.method == 'GET':
        articleForm = ArticleForm(instance=articleToUpdate)
        return render(request, template, {'articleForm':articleForm, 'article':articleToUpdate})
    # POST
    articleForm = ArticleForm(request.POST, instance=articleToUpdate)
    if not articleForm.is_valid():
        return render(request, template, {'articleForm':articleForm, 'article':articleToUpdate})
    articleForm.save()
    messages.success(request, '文章已修改')
    return redirect('article:articleRead', articleId=articleId)

def articleDelete(request, articleId):
    '''
    Delete the article instance:
        1. Render the article page if the method is GET
        2. Get the article to delete; redirect to 404 if not found
    '''
    if request.method=='GET':
        return article(request)
    # POST
    articleToDelete = get_object_or_404(Article, id=articleId)
    articleToDelete.delete()
    messages.success(request, '文章已刪除')
    return redirect('article:article') 
 
def articleSearch(request):
    '''
    Search for articles:
        1. Get the "searchTerm" from the HTML page
        2. Use "searchTerm" for filtering
    '''
    searchTerm = request.GET.get('searchTerm')
    articles = Article.objects.filter(Q(title__icontains=searchTerm)|Q(content__icontains=searchTerm))
    context = {'articles':articles, 'searchTerm':searchTerm}
    return render(request, 'article/articleSearch.html', context)

def commentCreate(request, articleId):
    '''
    Create a new comment
        1. Get the object or 404
        2. If method is GET, render the original page (User is messing around)
        3. If method is POST, perform form validation. Display error
        messages if the form is invalid
        4. Save the form to the model and redirect to the article page
    '''
    articleToComment = get_object_or_404(Article, id=articleId)
    if request.method=='GET':
    # User issues the GET request from the URL field
        return articleRead(request, articleToComment.id)
    # POST
    content = request.POST.get('comment')
    if content:
        Comment.objects.create(article=articleToComment, content=content)
    return redirect('article:articleRead', articleId=articleId)  
def addLike(request, articleId):
    articleToLike = get_object_or_404(Article, id=articleId)
    articleToLike.likes += 1
    articleToLike.save()
    return redirect('article:articleRead', articleId=articleId)   