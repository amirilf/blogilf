from django.urls import path
from .views import index_view,article_view,add_article_view

app_name = 'blog'

urlpatterns = [
    path('', index_view , name='index'),
    path('article/<slug:slug>', article_view, name='article'),
    path('new', add_article_view, name='new-article'),
]
