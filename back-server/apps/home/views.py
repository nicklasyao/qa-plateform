from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
import json


# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return redirect('login/')
    return render(request, "index.html")


# def get_user(request):
#     users = AuthUser.objects.all()
#     return render(request, 'user.html', {'users': users})


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


# 服务api
def logging_in(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        user_name = body.get('username')
        pass_word = body.get('password')

        user = authenticate(username=user_name, password=pass_word)

        if user is not None:
            login(request, user)
            data = {'name': user.username}
            return JsonResponse(_get_response_json_dic(data))
        else:
            return JsonResponse(_get_response_json_dic('', -1, '用户名或密码错误'))
    # get
    return JsonResponse(_get_response_json_dic('', -1, '无效请求'))


def log_user_out(request):
    logout(request)
    return redirect('/login/')


# 封装rest结果
def _get_response_json_dic(data, code=0, message='Success'):
    result_data = {
        'code': code,
        'message': message,
        'data': data
    }
    return result_data
