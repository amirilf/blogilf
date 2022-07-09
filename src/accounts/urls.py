from django.urls import path,re_path
from .views import login_view,logout_view,sign_up_view,profile_view

app_name = 'accounts'

urlpatterns = [
    path('login/', login_view , name='login'),
    path('logout/', logout_view , name='logout'),
    path('signup/', sign_up_view , name='signup'),
    
    re_path('^u/(?P<username>[\w.@+-]+)/$', profile_view , name='profile'),
    re_path('^u/(?P<username>[\w.@+-]+)/following/$', profile_view , name='following'),
    re_path('^u/(?P<username>[\w.@+-]+)/followers/$', profile_view , name='followers'),
    

]
