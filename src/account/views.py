from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,logout, login
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse
from django.utils.http import is_safe_url
from django.conf import settings


# profile

@login_required
def profile_view(request):
    return HttpResponse('profile')



# auth


def safe_redirect_after_login(request):
    next = request.GET.get("next", None)
    if next is None:
        return redirect(settings.LOGIN_REDIRECT_URL)
    elif not is_safe_url(
            url=next,
            allowed_hosts={request.get_host()},
            require_https=request.is_secure()):
        return redirect(settings.LOGIN_REDIRECT_URL)
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
        if request.user.is_authenticated:
            return redirect('blog:index')
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
            return redirect('blog:index')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('blog:index')
    raise Http404
