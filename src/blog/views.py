from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_list_or_404, get_object_or_404, redirect, render

from accounts.models import User
from .models import Article

from .forms import NewArticleForm


# Home view
def index_view(request):
    articles = Article.objects.select_related('author').filter(status=True)
    context = {
        'articles':articles
    }
    return render(request,'index.html',context)


# View an specific article
def article_view(request,username,slug):
    article = get_object_or_404(Article,author__username=username,slug=slug)
    context = {
        'article': article,
        'author' : username
    }
    return render(request,'article.html',context)



# User articles
def user_articles_view(request,username):
    articles = Article.objects.filter(author__username=username)
    context = {
        'articles': articles,
        'author'  : username,
    }
    return render(request,'user_articles.html',context)


# Add an article
@login_required
def add_article_view(request):
    if request.method == 'POST':
        form = NewArticleForm(request.user,False,request.POST,request.FILES)
        if form.is_valid():
            new_article = form.save(commit=False)
            new_article.author = User.objects.get(pk=request.user.pk) 
            form.save()
            return redirect('blog:articles')
    else:
        form = NewArticleForm(request.user,False)
    context = {
        'form': form
    }
    return render(request, 'new_article.html', context)


# Edit the article
def edit_article_view(request,username,slug):
    if request.user.username == username:
        
        article = get_object_or_404(Article,author__username=username,slug=slug)
        last_uploaded_image = article.thumbnail

        if request.method=="POST":
            form = NewArticleForm(request.user,True,request.POST,request.FILES,instance=article)
            if form.is_valid():
                form.save()
                return redirect('blog:article',username=username,slug=form.cleaned_data['slug'])
        else:
            form = NewArticleForm(request.user,True,instance=article)
        
        context = {
            'form': form,
            'image':last_uploaded_image
        }

        return render(request,'edit_article.html',context)
    raise Http404()


# Delete the article
def delete_article_view(request,username,slug):
    if request.user.username == username:
        
        article = get_object_or_404(Article,author__username=username,slug=slug)
        
        if request.method=="POST":
            article.delete()
            return redirect('blog:user-articles',username=username)
        else:
            return render(request,'delete_article.html')
    raise Http404()


def tag_view(request,slug):
    articles = get_list_or_404(Article,tags__contains=f' {slug} ')
    context = {
        'tag' : slug,
        'articles':articles,
    }
    return render(request,'tag.html',context)