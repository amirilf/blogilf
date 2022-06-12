from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from account.models import User
from .forms import NewArticleForm
from .models import Article

def index_view(request):

    articles = Article.objects.filter(status=True)
    context = {
        'articles':articles
    }
    return render(request,'index.html',context)

def article_view(request,slug):

    article = Article.objects.get(slug=slug)
    context = {
        'article':article
    }
    return render(request,'article.html',context)

@login_required
def add_article_view(request):
    if request.method == 'POST':
        form = NewArticleForm(request.POST,request.FILES)
        if form.is_valid():
            new_article = form.save(commit=False)
            new_article.author = User.objects.get(pk=request.user.pk) 
            form.save()
            return redirect('blog:index')
    else:
        form = NewArticleForm()
    
    return render(request, 'new-article.html', {'form': form})
