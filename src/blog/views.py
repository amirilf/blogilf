from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import NewArticleForm


def index_view(request):
    return render(request,'index.html')

def article_view(request):
    return render(request,'article.html')

@login_required
def add_article_view(request):
    if request.method == 'POST':
        form = NewArticleForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog:index')
    else:
        form = NewArticleForm()
    
    return render(request, 'new-article.html', {'form': form})
