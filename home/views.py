from django.shortcuts import render, redirect
from .models import AuthUser
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return redirect('login/')
    return render(request, "index.html")


def get_user(request):
    users = AuthUser.objects.all()
    return render(request, 'user.html', {'users': users})


def log_user_in(request):
    if request.POST:
        user_name = request.POST.get('username')
        pass_word = request.POST.get('password')

        user = authenticate(username=user_name, password=pass_word)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {'msg': '用户名或密码错误'})
    # get
    return render(request, 'login.html', {})


def log_user_out(request):
    logout(request)
    return redirect('/login/')
