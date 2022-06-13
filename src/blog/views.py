from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from account.models import User
from .models import Article

from .forms import NewArticleForm


def index_view(request):

    articles = Article.objects.filter(status=True).order_by('-created')
    context = {
        'articles':articles
    }
    return render(request,'index.html',context)

def article_view(request,username,slug):
    article = Article.objects.get(author__username=username,slug=slug)
    context = {
        'article':article
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
        print(form.errors)
    else:
        form = NewArticleForm(request.user)
    
    return render(request, 'new-article.html', {'form': form})

def user_view(request,username):
    user = User.objects.get(username=username)
    context = {
        'user':user
    }
    return render(request,'user.html',context)
