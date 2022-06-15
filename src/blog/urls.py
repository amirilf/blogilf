from django.urls import path,re_path
from .views import (
    index_view,
    article_view,
    add_article_view,
    edit_article_view,
    delete_article_view,
    user_view,
    user_articles_view
)

app_name = 'blog'

urlpatterns = [
    path('', index_view , name='index'),
    re_path('^user/(?P<username>[\w.@+-]+)$', user_view , name='user'),
    re_path('^user/(?P<username>[\w.@+-]+)/articles$', user_articles_view , name='user-articles'),
    re_path('^user/(?P<username>[\w.@+-]+)/article/(?P<slug>[-\w]+)$', article_view, name='article'),
    re_path('^user/(?P<username>[\w.@+-]+)/article/(?P<slug>[-\w]+)/edit$', edit_article_view, name='article-edit'),
    re_path('^user/(?P<username>[\w.@+-]+)/article/(?P<slug>[-\w]+)/delete$', delete_article_view, name='article-delete'),
    path('new', add_article_view, name='new-article'),
]
