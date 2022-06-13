from django.urls import path,re_path
from .views import index_view,article_view,add_article_view,user_view

app_name = 'blog'

urlpatterns = [
    path('', index_view , name='index'),
    re_path('^user/(?P<username>[\w.@+-]+)$', user_view , name='user'),
    re_path(r'^user/(?P<username>[\w.@+-]+)/article/(?P<slug>[-\w]+)$', article_view, name='article'),
    path('new', add_article_view, name='new-article'),
]
