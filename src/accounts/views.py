from django.http import Http404
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth import authenticate,logout, login,get_user_model
from django.utils.http import is_safe_url
from .forms import SignUpForm
from .models import UserFollowing
    

# profile

def profile_view(request,username):
    
    user_object = get_object_or_404(get_user_model(),username=username)
    btn = str
    
    if request.user.is_authenticated:
        btn = 'Follow'
        if request.method == 'POST':
            
            object = UserFollowing.objects.get_or_create(user_id=request.user,following_user_id=user_object)
        
            if object[1]:
                # following object created
                btn = 'Unfollow'
            else:
                # following object exists so delete
                object[0].delete()
        
        # GET
        else:
            following_object = UserFollowing.objects.filter(user_id=request.user,following_user_id=user_object).exists()
            if following_object:
                btn = 'Unfollow'

    context = {
        'user_object':user_object,
        'submit_btn' : btn
    }

    return render(request,'user.html',context)


def following_view(request,username):
    user_object = get_object_or_404(get_user_model(),username=username)
    following_objects = get_user_model().objects.filter(followers__user_id=user_object).only('username')

    context = {
        'user_object':user_object,
        'following_objects' : following_objects
    }

    return render(request,'following.html',context)


def followers_view(request,username):
    user_object = get_object_or_404(get_user_model(),username=username)
    followers_objects = get_user_model().objects.filter(following__following_user_id=user_object).only('username')

    context = {
        'user_object':user_object,
        'followers_objects' : followers_objects
    }

    return render(request,'followers.html',context)




# auth stuff

def safe_redirect_after_login(request):
    next = request.GET.get("next", None)
    if next is None:
        return redirect('accounts:login')
    elif not is_safe_url(
            url=next,
            allowed_hosts={request.get_host()},
            require_https=request.is_secure()):
        return redirect('accounts:login')
    else:
        return redirect(next)

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return safe_redirect_after_login(request)
        else:
            return render(request, 'login.html', {'error':'The username or password are incorrect'})
    else:
        # GET method
        if request.user.is_authenticated:
            # It's a logged in user so there is no need to show login page
            return redirect('blog:articles')
        else:
            # It's an anonymous user
            return render(request, 'login.html')

def sign_up_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('blog:articles')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('blog:articles')
    raise Http404