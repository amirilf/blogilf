from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def index_view(request):
    return render(request,'index.html')

def about_view(request):
    return render(request,'about.html')

def article_view(request):
    return render(request,'article.html')

@login_required
def add_article_view(request):
    return render(request,'new-article.html')
