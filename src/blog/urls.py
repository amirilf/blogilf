from django.urls import path
from .views import index_view,about_view,article_view

app_name = 'blog'

urlpatterns = [
    path('', index_view , name='index'),
    path('about', about_view , name='about'),
    path('article', article_view),
]
