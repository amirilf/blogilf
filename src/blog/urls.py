from django.urls import path,re_path
from .views import (
    index_view,
    article_view,
    add_article_view,
    edit_article_view,
    delete_article_view,
    tag_view,
    user_articles_view,
)

app_name = 'blog'

urlpatterns = [
    # path('', index_view , name='index'),

    # path('new', add_article_view, name='new-article'),

    # re_path('^user/(?P<username>[\w.@+-]+)$', user_view , name='user'),
    # re_path('^user/(?P<username>[\w.@+-]+)/articles$', user_articles_view , name='user-articles'),
    # re_path('^user/(?P<username>[\w.@+-]+)/article/(?P<slug>[-\w]+)$', article_view, name='article'),
    # re_path('^user/(?P<username>[\w.@+-]+)/article/(?P<slug>[-\w]+)/edit$', edit_article_view, name='article-edit'),
    # re_path('^user/(?P<username>[\w.@+-]+)/article/(?P<slug>[-\w]+)/delete$', delete_article_view, name='article-delete'),

    # re_path('^tags/(?P<slug>[a-z0-9](-?[a-z0-9])*)$',tag_view,name='tag'),

    #====
    
    # CRUD
    path('new/',add_article_view, name='new-article'),
    re_path('^(?P<username>[\w.@+-]+)/(?P<slug>[-\w]+)/$',article_view,name='article'),
    re_path('^(?P<username>[\w.@+-]+)/(?P<slug>[-\w]+)/edit/$',edit_article_view,name='article-edit'),
    re_path('^(?P<username>[\w.@+-]+)/(?P<slug>[-\w]+)/delete/$',delete_article_view,name='article-delete'),
    
    # like
    re_path('^(?P<username>[\w.@+-]+)/(?P<slug>[-\w]+)/like/$',article_view,name='article-like'),

    # lists
    path('',index_view, name='articles'),
    re_path('^(?P<username>[\w.@+-]+)/$', user_articles_view,name='user-articles'),
    re_path('^tag/(?P<slug>[a-z0-9](-?[a-z0-9])*)$',tag_view, name='tag'),

]
