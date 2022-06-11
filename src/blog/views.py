from django.shortcuts import render


def index_view(request):
    return render(request,'index.html')

def about_view(request):
    return render(request,'about.html')

def article_view(request):
    return render(request,'article.html')

def add_article_view(request):
    return render(request,'new-article.html')
