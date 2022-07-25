from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.shortcuts import get_list_or_404, get_object_or_404, redirect, render
from .models import Article
from .decorators import user_is_author
from .forms import NewArticleForm


# Articles view
def articles_view(request):
    
    print(request.GET.get('name'))
    # date
    # new to old nto
    # old to new otn
    # most viewed mv
    # most favorite mf

    articles = Article.objects.select_related('author').filter(status=True)
    context = {
        'articles':articles
    }
    return render(request,'index.html',context)


# View an specific article
def article_view(request,username,slug):
    article = get_object_or_404(Article,author__username=username,slug=slug)
    
    article.views += 1
    article.save()

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
            new_article.author = get_user_model().objects.get(pk=request.user.pk) 
            form.save()
            return redirect('blog:articles')
    else:
        form = NewArticleForm(request.user,False)
    context = {
        'form': form
    }
    return render(request, 'new_article.html', context)


# Edit the article
@user_is_author
def edit_article_view(request,username,slug):
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


# Delete the article
@user_is_author
def delete_article_view(request,username,slug):
    article = get_object_or_404(Article,author__username=username,slug=slug)
        
    if request.method=="POST":
        article.delete()
        return redirect('blog:user-articles',username=username)
    else:
        return render(request,'delete_article.html')


def tag_view(request,slug):
    articles = get_list_or_404(Article,tags__contains=f' {slug} ')
    context = {
        'tag' : slug,
        'articles':articles,
    }
    return render(request,'tag.html',context)