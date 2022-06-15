from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from accounts.models import User
from .models import Article

from .forms import NewArticleForm


def index_view(request):

    articles = Article.objects.select_related('author').filter(status=True)
    context = {
        'articles':articles
    }
    return render(request,'index.html',context)

def article_view(request,username,slug):
    article = Article.objects.get(author__username=username,slug=slug)
    context = {
        'article': article,
        'author' : username
    }
    return render(request,'article.html',context)

@login_required
def add_article_view(request):
    if request.method == 'POST':
        form = NewArticleForm(request.user,request.POST,request.FILES)
        if form.is_valid():
            new_article = form.save(commit=False)
            new_article.author = User.objects.get(pk=request.user.pk) 
            form.save()
            return redirect('blog:index')
    else:
        form = NewArticleForm(request.user)
    
    return render(request, 'new-article.html', {'form': form})

def user_view(request,username):
    user = User.objects.get(username=username)
    context = {
        'user_object':user
    }
    return render(request,'user.html',context)

def user_articles_view(request,username):
    print(username)
    articles = Article.objects.filter(author__username=username)
    print(articles)
    context = {
        'articles': articles,
        'author'  : username,
    }
    return render(request,'user-articles.html',context)
