from django.shortcuts import render, redirect
import datetime
from django.contrib import messages

from blog.settings import LOGIN_URL

def main(request):
    '''
    Render the main page
    '''
    now = datetime.datetime.now()
    context = {'like':'Django 很棒', 'now':now}
    return render(request, 'main/main.html', context)


def about(request):
    '''
    Render the "about" page
    '''
    return render(request, 'main/about.html')


def contact(request):
    '''
    Render the "contact" page
    '''
    return render(request, 'main/contact.html')


def admin_required(func):
    def auth(request, *args, **kwargs):
        if not request.user.is_superuser:
            messages.error(request, '請以管理者身份登入')
            return redirect('account:login')
        return func(request, *args, **kwargs)
    return auth